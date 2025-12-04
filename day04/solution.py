"""
Advent of Code 2025 - Day 4: Printing Department

The forklifts can only access a roll of paper if there are fewer than four rolls 
of paper in the eight adjacent positions. Count how many rolls can be accessed.
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def solve_part1(data):
    """
    Part 1: Count rolls of paper accessible by forklifts.
    
    A roll is accessible if it has fewer than 4 rolls in the 8 adjacent positions.
    
    Args:
        data: List of strings representing the grid
    
    Returns:
        Number of accessible rolls
    """
    if not data:
        return 0
    
    # Parse grid
    grid = [line.strip() for line in data if line.strip()]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Directions for 8 adjacent cells (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),           (0, 1),   # left, right
        (1, -1),  (1, 0),  (1, 1)    # bottom-left, bottom, bottom-right
    ]
    
    accessible_count = 0
    
    # Check each position in the grid
    for r in range(rows):
        for c in range(cols):
            # Only check positions with paper rolls
            if grid[r][c] == '@':
                # Count adjacent paper rolls
                adjacent_rolls = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check if position is within bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            adjacent_rolls += 1
                
                # A roll is accessible if it has fewer than 4 adjacent rolls
                if adjacent_rolls < 4:
                    accessible_count += 1
    
    return accessible_count


def solve_part2(data):
    """
    Part 2: Count total rolls that can be removed through iterative process.
    
    Once accessible rolls are removed, more rolls may become accessible.
    Continue until no more rolls can be removed.
    
    Args:
        data: List of strings representing the grid
    
    Returns:
        Total number of rolls that can be removed
    """
    if not data:
        return 0
    
    # Parse grid into a mutable 2D list
    grid = [list(line.strip()) for line in data if line.strip()]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Directions for 8 adjacent cells
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    total_removed = 0
    
    # Keep removing accessible rolls until none are left
    while True:
        # Find all accessible rolls in current state
        accessible = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    # Count adjacent rolls
                    adjacent_rolls = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '@':
                                adjacent_rolls += 1
                    
                    # Roll is accessible if it has fewer than 4 adjacent rolls
                    if adjacent_rolls < 4:
                        accessible.append((r, c))
        
        # If no rolls are accessible, we're done
        if not accessible:
            break
        
        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = '.'
        
        total_removed += len(accessible)
    
    return total_removed


def main():
    """Main entry point for Day 4 solution."""
    # Example test data
    example_data = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."
    ]
    
    # Test with example
    print("=== Day 4: Printing Department ===\n")
    
    if example_data:
        print("Testing with example:")
        example_part1 = solve_part1(example_data)
        print(f"  Part 1: {example_part1} (expected: 13)")
        
        example_part2 = solve_part2(example_data)
        print(f"  Part 2: {example_part2} (expected: 43)")
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
