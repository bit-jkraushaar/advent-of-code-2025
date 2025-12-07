"""Debug script for Day 7"""
from collections import deque

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

# Parse the grid
grid = [list(line) for line in example_data]
rows = len(grid)
cols = len(grid[0])

# Find starting position 'S'
start_pos = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start_pos = (r, c)
            print(f"Found S at row {r}, col {c}")
            break
    if start_pos:
        break

# BFS to simulate beam propagation
queue = deque([(start_pos[0], start_pos[1], 'D')])
visited = set()
split_count = 0

step = 0
while queue:
    r, c, direction = queue.popleft()
    
    # Check if already visited this state
    if (r, c, direction) in visited:
        continue
    visited.add((r, c, direction))
    
    print(f"Step {step}: At ({r}, {c}) going {direction}, queue size: {len(queue)}")
    
    # Move in the current direction
    if direction == 'D':
        next_r, next_c = r + 1, c
    elif direction == 'L':
        next_r, next_c = r, c - 1
    else:  # 'R'
        next_r, next_c = r, c + 1
    
    # Check bounds
    if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
        print(f"  -> Beam exits at ({next_r}, {next_c})")
        step += 1
        continue
    
    cell = grid[next_r][next_c]
    print(f"  -> Next cell ({next_r}, {next_c}) = '{cell}'")
    
    if cell == '^':
        split_count += 1
        print(f"  -> SPLIT #{split_count}! Creating L and R beams")
        queue.append((next_r, next_c, 'L'))
        queue.append((next_r, next_c, 'R'))
    elif cell == '.' or cell == 'S':
        queue.append((next_r, next_c, direction))
    
    step += 1
    if step > 100:  # Safety limit
        print("SAFETY LIMIT REACHED")
        break

print(f"\nTotal splits: {split_count}")
print(f"Expected: 21")
