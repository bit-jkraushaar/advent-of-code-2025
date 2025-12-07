"""
Advent of Code 2025 - Day 7: Laboratories

A tachyon beam enters a manifold at location 'S' and moves downward.
The beam passes through empty space '.' but splits when encountering '^'.
When a beam hits a splitter, it stops and emits two new beams left and right.
"""

import os
import sys
from collections import deque

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def solve_part1(data):
    """
    Part 1: Count how many times the beam is split
    
    Strategy:
    - All beams move downward
    - When a downward-moving beam hits '^', it stops and creates two new beams
    - The two new beams start at positions immediately left and right of the splitter
    - Those beams also move downward and can trigger more splits
    - Count the total number of splits
    
    Args:
        data: List of strings representing the tachyon manifold grid
    
    Returns:
        Total number of times the beam is split
    """
    # Parse the grid
    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find starting position 'S'
    start_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r, c)
                break
        if start_pos:
            break
    
    if not start_pos:
        return 0
    
    # BFS to simulate beam propagation
    # Each beam is represented by its current column position (all beams move down)
    # State: (row, col) - position of beam
    queue = deque([start_pos])
    visited = set()
    split_count = 0
    
    while queue:
        r, c = queue.popleft()
        
        # Check if already visited this position
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        # Move downward
        next_r = r + 1
        
        # Check bounds
        if next_r >= rows:
            continue  # Beam exits the manifold
        
        cell = grid[next_r][c]
        
        if cell == '^':
            # Hit a splitter - beam splits
            split_count += 1
            # Create two new beams: one at left, one at right of the splitter
            # Both beams continue moving downward from their new positions
            left_c = c - 1
            right_c = c + 1
            if left_c >= 0:
                queue.append((next_r, left_c))
            if right_c < cols:
                queue.append((next_r, right_c))
        elif cell == '.' or cell == 'S':
            # Continue downward from the same column
            queue.append((next_r, c))
    
    return split_count


def solve_part2(data):
    """
    Part 2: Count the number of timelines using many-worlds interpretation
    
    Each timeline represents a unique path through the manifold.
    When a particle hits a splitter, the timeline splits into 2 timelines.
    Count the total number of distinct timelines (paths) that reach the exit.
    
    Key insight: Use dynamic programming to count paths.
    - dp[position] = number of distinct paths that reach this position
    - When hitting a splitter, the path count doubles (splits to left and right)
    - Sum all path counts that exit the manifold
    
    Args:
        data: List of strings representing the tachyon manifold grid
    
    Returns:
        Total number of unique timelines
    """
    # Parse the grid
    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find starting position 'S'
    start_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r, c)
                break
        if start_pos:
            break
    
    if not start_pos:
        return 0
    
    from collections import defaultdict, deque
    
    # BFS with path counting
    # State: (row, col)
    # path_count[position] = number of distinct paths that reached this position
    queue = deque([start_pos])
    path_count = defaultdict(int)
    path_count[start_pos] = 1
    visited = set()
    
    while queue:
        pos = queue.popleft()
        
        if pos in visited:
            continue
        visited.add(pos)
        
        r, c = pos
        count = path_count[pos]
        
        # Move downward
        next_r = r + 1
        
        # Check bounds
        if next_r >= rows:
            # This position exits - its path count contributes to total timelines
            # (already counted in path_count)
            continue
        
        cell = grid[next_r][c]
        
        if cell == '^':
            # Hit a splitter - paths split into left and right
            # Each path that reached here creates 2 new paths
            left_c = c - 1
            right_c = c + 1
            if left_c >= 0:
                left_pos = (next_r, left_c)
                path_count[left_pos] += count
                if left_pos not in visited:
                    queue.append(left_pos)
            if right_c < cols:
                right_pos = (next_r, right_c)
                path_count[right_pos] += count
                if right_pos not in visited:
                    queue.append(right_pos)
        elif cell == '.' or cell == 'S':
            # Continue downward - same number of paths
            next_pos = (next_r, c)
            path_count[next_pos] += count
            if next_pos not in visited:
                queue.append(next_pos)
    
    # Count total timelines: sum of path counts for all positions in the last row
    # or positions that would exit
    total_timelines = 0
    for (r, c), count in path_count.items():
        # Check if this position would exit on next step
        if r + 1 >= rows:
            total_timelines += count
        elif grid[r + 1][c] not in ['.', '^', 'S']:
            # Would exit (no valid next cell)
            total_timelines += count
    
    return total_timelines


def main():
    """Main entry point for Day 7 solution."""
    # Example test data
    example_data = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]
    
    # Test with example
    print("=== Day 7: Laboratories ===\n")
    
    if example_data:
        print("Testing with example:")
        example_part1 = solve_part1(example_data)
        print(f"  Part 1: {example_part1} (expected: 21)")
        
        example_part2 = solve_part2(example_data)
        print(f"  Part 2: {example_part2} (expected: 40)")
        print()
    
    # Solve actual puzzle
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    
    try:
        data = read_input(input_file)
        
        part1_answer = solve_part1(data)
        print("Puzzle answers:")
        print(f"  Part 1: {part1_answer}")
        
        part2_answer = solve_part2(data)
        print(f"  Part 2: {part2_answer}")
        
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        print("Please add your puzzle input to solve the actual puzzle.")


if __name__ == "__main__":
    main()
