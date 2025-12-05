"""
Advent of Code 2025 - Day 5: Cafeteria

Determine which available ingredient IDs are fresh based on fresh ID ranges.
Fresh ID ranges are inclusive and can overlap. Count how many available IDs
fall within any fresh range.
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input_groups


def solve_part1(data):
    """
    Part 1: Count how many available ingredient IDs are fresh.
    
    An ingredient ID is fresh if it falls within any of the fresh ID ranges.
    Ranges are inclusive and can overlap.
    
    Args:
        data: Two groups - first group is fresh ID ranges (e.g., "3-5"),
              second group is available ingredient IDs (e.g., "1")
    
    Returns:
        Number of fresh ingredient IDs
    """
    # Parse the input groups
    fresh_ranges = data[0]
    available_ids = data[1]
    
    # Parse fresh ranges into list of (start, end) tuples
    ranges = []
    for range_str in fresh_ranges:
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    
    # Parse available IDs into integers
    ids = [int(id_str) for id_str in available_ids]
    
    # Count how many IDs are fresh (fall within any range)
    fresh_count = 0
    for ingredient_id in ids:
        is_fresh = any(start <= ingredient_id <= end for start, end in ranges)
        if is_fresh:
            fresh_count += 1
    
    return fresh_count


def solve_part2(data):
    """
    Part 2: Count total ingredient IDs considered fresh by the ranges.
    
    Find all unique ingredient IDs that fall within any of the fresh ID ranges.
    The available IDs section is now irrelevant - we just want to know how many
    total IDs are covered by all the fresh ranges combined.
    
    Uses range merging optimization: instead of creating a set of millions of IDs,
    we merge overlapping/adjacent ranges and count the total span.
    
    Args:
        data: Two groups - first group is fresh ID ranges (e.g., "3-5")
              (second group is ignored for part 2)
    
    Returns:
        Total count of ingredient IDs considered fresh by the ranges
    """
    # Parse the fresh ranges
    fresh_ranges = data[0]
    
    # Parse fresh ranges into list of (start, end) tuples
    ranges = []
    for range_str in fresh_ranges:
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    
    # Sort ranges by start position
    ranges.sort()
    
    # Merge overlapping or adjacent ranges
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent - extend the last merged range
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # Non-overlapping - add as new range
            merged.append((start, end))
    
    # Count total IDs in merged ranges
    total = 0
    for start, end in merged:
        total += end - start + 1
    
    return total


def main():
    """Main entry point for Day 5 solution."""
    # Example test data
    example_data = [
        ['3-5', '10-14', '16-20', '12-18'],
        ['1', '5', '8', '11', '17', '32']
    ]
    
    # Test with example
    print("=== Day 5: Cafeteria ===\n")
    
    if example_data:
        print("Testing with example:")
        example_part1 = solve_part1(example_data)
        print(f"  Part 1: {example_part1} (expected: 3)")
        
        example_part2 = solve_part2(example_data)
        print(f"  Part 2: {example_part2} (expected: 14)")
        print()
    
    # Solve actual puzzle
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    
    try:
        data = read_input_groups(input_file)
        
        if not data or len(data) < 2:
            print(f"Input file is empty or incomplete: {input_file}")
            print("Please add your puzzle input to solve the actual puzzle.")
            return
        
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
