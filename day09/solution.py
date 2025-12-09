"""
Advent of Code 2025 - Day 9: Movie Theater

Find the largest rectangle that can be formed using red tiles as opposite corners.
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def solve_part1(data):
    """
    Part 1: Find the largest rectangle area using red tiles as opposite corners
    
    Args:
        data: List of strings in format "x,y" representing red tile coordinates
    
    Returns:
        Largest rectangle area
    """
    # Parse red tile coordinates
    red_tiles = []
    for line in data:
        x, y = map(int, line.split(','))
        red_tiles.append((x, y))
    
    max_area = 0
    
    # Try every pair of red tiles as opposite corners
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            
            # For two points to be opposite corners, they must differ in both x and y
            if x1 != x2 and y1 != y2:
                # Calculate rectangle area (add 1 to include both corners)
                width = abs(x2 - x1) + 1
                height = abs(y2 - y1) + 1
                area = width * height
                max_area = max(max_area, area)
    
    return max_area


def solve_part2(data):
    """
    Part 2: Find largest rectangle using only red and green tiles
    
    Uses coordinate compression to work in compact space.
    
    Args:
        data: List of strings in format "x,y" representing red tile coordinates
    
    Returns:
        Largest rectangle area using only red/green tiles
    """
    # Parse red tile coordinates
    red_tiles = []
    for line in data:
        x, y = map(int, line.split(','))
        red_tiles.append((x, y))
    
    # Coordinate compression: map actual coords to compressed indices
    all_x = sorted(set(x for x, y in red_tiles))
    all_y = sorted(set(y for x, y in red_tiles))
    
    x_to_idx = {x: i for i, x in enumerate(all_x)}
    y_to_idx = {y: i for i, y in enumerate(all_y)}
    
    # Convert red tiles to compressed coordinates
    compressed_red = [(x_to_idx[x], y_to_idx[y]) for x, y in red_tiles]
    
    # Build compressed grid
    width = len(all_x)
    height = len(all_y)
    grid = [[False] * width for _ in range(height)]
    
    # Mark red tiles
    for cx, cy in compressed_red:
        grid[cy][cx] = True
    
    # Add green connecting lines
    for i in range(len(compressed_red)):
        cx1, cy1 = compressed_red[i]
        cx2, cy2 = compressed_red[(i + 1) % len(compressed_red)]
        
        if cx1 == cx2:  # Vertical
            for cy in range(min(cy1, cy2), max(cy1, cy2) + 1):
                grid[cy][cx1] = True
        else:  # Horizontal
            for cx in range(min(cx1, cx2), max(cx1, cx2) + 1):
                grid[cy1][cx] = True
    
    # Fill interior using scanline on compressed grid
    for cy in range(height):
        # Find crossings for this row
        crossings = []
        for i in range(len(compressed_red)):
            cx1, cy1 = compressed_red[i]
            cx2, cy2 = compressed_red[(i + 1) % len(compressed_red)]
            
            if cy1 != cy2 and min(cy1, cy2) < cy <= max(cy1, cy2):
                # Linear interpolation in compressed space
                t = (cy - cy1) / (cy2 - cy1)
                cx_cross = cx1 + t * (cx2 - cx1)
                crossings.append(cx_cross)
        
        if crossings:
            crossings.sort()
            for i in range(0, len(crossings) - 1, 2):
                cx_start = int(crossings[i])
                cx_end = int(crossings[i + 1])
                for cx in range(cx_start, cx_end + 1):
                    grid[cy][cx] = True
    
    # Find largest rectangle with red corners
    max_area = 0
    
    for i in range(len(red_tiles)):
        x1, y1 = red_tiles[i]
        cx1, cy1 = x_to_idx[x1], y_to_idx[y1]
        
        for j in range(i + 1, len(red_tiles)):
            x2, y2 = red_tiles[j]
            cx2, cy2 = x_to_idx[x2], y_to_idx[y2]
            
            if cx1 == cx2 or cy1 == cy2:
                continue
            
            # Check compressed rectangle
            min_cx, max_cx = min(cx1, cx2), max(cx1, cx2)
            min_cy, max_cy = min(cy1, cy2), max(cy1, cy2)
            
            valid = True
            for cy in range(min_cy, max_cy + 1):
                if not valid:
                    break
                for cx in range(min_cx, max_cx + 1):
                    if not grid[cy][cx]:
                        valid = False
                        break
            
            if valid:
                # Calculate area in ORIGINAL coordinates
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                max_area = max(max_area, area)
    
    return max_area


def main():
    """Main entry point for Day 9 solution."""
    # Example test data
    example_data = [
        "7,1",
        "11,1",
        "11,7",
        "9,7",
        "9,5",
        "2,5",
        "2,3",
        "7,3"
    ]
    
    # Test with example
    print("=== Day 9: Movie Theater ===\n")
    
    if example_data:
        print("Testing with example:")
        example_part1 = solve_part1(example_data)
        print(f"  Part 1: {example_part1} (expected: 50)")
        
        example_part2 = solve_part2(example_data)
        print(f"  Part 2: {example_part2} (expected: 24)")
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
