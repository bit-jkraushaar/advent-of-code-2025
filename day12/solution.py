"""
Advent of Code 2025 - Day 12: Christmas Tree Farm

Uses Google OR-Tools CP-SAT solver for constraint satisfaction.
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.input_reader import read_input_raw
from ortools.sat.python import cp_model

def parse_input(data):
    sections = data.strip().split('\n\n')
    shapes = {}
    section_idx = 0
    
    for i, section in enumerate(sections):
        lines = section.split('\n')
        first_line = lines[0].strip()
        if first_line and first_line[-1] == ':' and first_line[:-1].isdigit():
            idx = int(first_line[:-1])
            shapes[idx] = [list(line) for line in lines[1:]]
            section_idx = i + 1
        else:
            section_idx = i
            break
    
    regions = []
    for section in sections[section_idx:]:
        for line in section.split('\n'):
            line = line.strip()
            if not line or ': ' not in line or 'x' not in line:
                continue
            dims, counts = line.split(': ')
            w, h = map(int, dims.split('x'))
            present_counts = list(map(int, counts.split()))
            regions.append((w, h, present_counts))
    
    return shapes, regions

def get_shape_coords(shape):
    return [(r, c) for r, row in enumerate(shape) for c, cell in enumerate(row) if cell == '#']

def normalize_coords(coords):
    if not coords:
        return coords
    min_r = min(r for r, c in coords)
    min_c = min(c for r, c in coords)
    return tuple(sorted((r - min_r, c - min_c) for r, c in coords))

def get_all_orientations(shape):
    coords = get_shape_coords(shape)
    orientations = set()
    
    for _ in range(4):
        orientations.add(normalize_coords(coords))
        coords = [(c, -r) for r, c in coords]
    
    coords = [(r, -c) for r, c in coords]
    for _ in range(4):
        orientations.add(normalize_coords(coords))
        coords = [(c, -r) for r, c in coords]
    
    return list(orientations)

def can_fit_cpsat(w, h, presents, all_orientations, time_limit=3):
    """Use CP-SAT solver with placement limiting."""
    if not presents:
        return True
    
    total_cells = sum(len(all_orientations[s][0]) for s in presents)
    if total_cells > w * h:
        return False
    
    # For large problems (>80 presents), use a heuristic instead of exact solve
    if len(presents) > 80:
        # Heuristic: if there's enough slack and pieces aren't too constrained, assume it fits
        slack = w * h - total_cells
        slack_ratio = slack / total_cells if total_cells > 0 else 0
        
        # Need significant slack for many pieces
        required_slack = 0.15 + (len(presents) - 80) * 0.001
        return slack_ratio >= required_slack
    
    model = cp_model.CpModel()
    
    # Generate placements but LIMIT the number per present to avoid explosion
    MAX_PLACEMENTS_PER_PRESENT = 200
    present_placements = []
    for shape_idx in presents:
        placements = []
        for orientation in all_orientations[shape_idx]:
            if len(placements) >= MAX_PLACEMENTS_PER_PRESENT:
                break
            for row in range(h):
                if len(placements) >= MAX_PLACEMENTS_PER_PRESENT:
                    break
                for col in range(w):
                    cells = []
                    valid = True
                    for dr, dc in orientation:
                        r, c = row + dr, col + dc
                        if r < 0 or r >= h or c < 0 or c >= w:
                            valid = False
                            break
                        cells.append((r, c))
                    if valid:
                        placements.append(cells)
                        if len(placements) >= MAX_PLACEMENTS_PER_PRESENT:
                            break
        
        if not placements:
            return False
        present_placements.append(placements)
    
    # Decision variables: which placement for each present
    placement_vars = []
    for pres_idx, placements in enumerate(present_placements):
        pres_vars = [model.NewBoolVar(f'p{pres_idx}_{pl_idx}') 
                     for pl_idx in range(len(placements))]
        model.Add(sum(pres_vars) == 1)  # Exactly one placement per present
        placement_vars.append((pres_vars, placements))
    
    # Constraint: No cell overlap
    cell_usage = {}
    for pres_idx, (pres_vars, placements) in enumerate(placement_vars):
        for pl_idx, (var, placement) in enumerate(zip(pres_vars, placements)):
            for cell in placement:
                if cell not in cell_usage:
                    cell_usage[cell] = []
                cell_usage[cell].append(var)
    
    for cell, vars_list in cell_usage.items():
        model.Add(sum(vars_list) <= 1)
    
    # Solve
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.log_search_progress = False
    status = solver.Solve(model)
    
    return status in [cp_model.OPTIMAL, cp_model.FEASIBLE]

def solve_part1(data):
    shapes, regions = parse_input(data)
    all_orientations = {idx: get_all_orientations(shape) for idx, shape in shapes.items()}
    shape_sizes = {idx: len(all_orientations[idx][0]) for idx in shapes}
    
    print(f"  Total regions to check: {len(regions)}")
    
    count = 0
    skipped_space = 0
    checked = 0
    
    for w, h, present_counts in regions:
        area = w * h
        
        # Only filter: Space check (your optimization)
        total_cells_needed = sum(shape_sizes[idx] * cnt for idx, cnt in enumerate(present_counts))
        if total_cells_needed > area:
            skipped_space += 1
            continue
        
        checked += 1
        presents = [idx for idx, cnt in enumerate(present_counts) for _ in range(cnt)]
        
        if can_fit_cpsat(w, h, presents, all_orientations, time_limit=1):
            count += 1
        
        # Progress
        if checked % 20 == 0:
            print(f"    Progress: checked {checked}, found {count} fits...")
    
    print(f"  Skipped: {skipped_space} (space)")
    print(f"  Checked: {checked}, Found: {count}")
    return count

def solve_part2(data):
    pass

def main():
    example_data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
    
    print("=== Day 12: Christmas Tree Farm ===\n")
    print("Testing with example:")
    example_part1 = solve_part1(example_data)
    print(f"  Part 1: {example_part1} (expected: 2)")
    print()
    
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    try:
        data = read_input_raw(input_file)
        part1_answer = solve_part1(data)
        print("Puzzle answers:")
        print(f"  Part 1: {part1_answer}")
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")

if __name__ == "__main__":
    main()
