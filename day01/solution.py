"""
Advent of Code 2025 - Day 1: Secret Entrance
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def solve_part1(rotations):
    """
    Part 1: Count how many times the dial points at 0 after any rotation.
    
    Args:
        rotations: List of rotation instructions (e.g., ["L68", "R48"])
    
    Returns:
        Number of times the dial points at 0 after a rotation completes
    """
    dial_position = 50  # Starting position
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]  # 'L' or 'R'
        distance = int(rotation[1:])  # The number of clicks
        
        if direction == 'L':
            dial_position = (dial_position - distance) % 100
        else:  # direction == 'R'
            dial_position = (dial_position + distance) % 100
        
        if dial_position == 0:
            zero_count += 1
    
    return zero_count


def solve_part2(rotations):
    """
    Part 2: Count all times the dial passes through 0 during any click.
    
    Args:
        rotations: List of rotation instructions (e.g., ["L68", "R48"])
    
    Returns:
        Number of times the dial points at 0 during any click
    """
    dial_position = 50  # Starting position
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]  # 'L' or 'R'
        distance = int(rotation[1:])  # The number of clicks
        
        # Count every click that passes through 0
        if direction == 'L':
            for _ in range(distance):
                dial_position = (dial_position - 1) % 100
                if dial_position == 0:
                    zero_count += 1
        else:  # direction == 'R'
            for _ in range(distance):
                dial_position = (dial_position + 1) % 100
                if dial_position == 0:
                    zero_count += 1
    
    return zero_count


def main():
    """Main entry point for Day 1 solution."""
    # Example test data
    example_rotations = [
        "L68", "L30", "R48", "L5", "R60",
        "L55", "L1", "L99", "R14", "L82"
    ]
    
    # Test with example
    print("=== Day 1: Secret Entrance ===\n")
    print("Testing with example:")
    example_part1 = solve_part1(example_rotations)
    example_part2 = solve_part2(example_rotations)
    print(f"  Part 1: {example_part1} (expected: 3)")
    print(f"  Part 2: {example_part2} (expected: 6)")
    print()
    
    # Solve actual puzzle
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    
    try:
        rotations = read_input(input_file)
        
        part1_answer = solve_part1(rotations)
        part2_answer = solve_part2(rotations)
        
        print("Puzzle answers:")
        print(f"  Part 1: {part1_answer}")
        print(f"  Part 2: {part2_answer}")
        
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        print("Please add your puzzle input to solve the actual puzzle.")


if __name__ == "__main__":
    main()
