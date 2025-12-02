"""
Advent of Code 2025 - Day 2: Gift Shop

Find invalid product IDs in the gift shop database. An invalid ID is one that
consists of some sequence of digits repeated exactly twice (e.g., 11, 6464, 123123).
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def is_invalid_id(num):
    """
    Check if a number is an invalid ID (a sequence of digits repeated twice).
    
    Args:
        num: Integer to check
    
    Returns:
        True if the number is invalid (repeated twice pattern), False otherwise
    """
    s = str(num)
    length = len(s)
    
    # Must have even length to be repeated twice
    if length % 2 != 0:
        return False
    
    # Check if first half equals second half
    mid = length // 2
    return s[:mid] == s[mid:]


def is_invalid_id_part2(num):
    """
    Check if a number is an invalid ID (a sequence of digits repeated at least twice).
    
    Args:
        num: Integer to check
    
    Returns:
        True if the number is invalid (repeated at least twice pattern), False otherwise
    """
    s = str(num)
    length = len(s)
    
    # Try all possible pattern lengths (from 1 to length//2)
    # The pattern must repeat at least twice
    for pattern_len in range(1, length // 2 + 1):
        # Check if the length is divisible by pattern length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repeats = length // pattern_len
            
            # Check if the pattern repeats at least twice
            if repeats >= 2 and pattern * repeats == s:
                return True
    
    return False


def solve_part1(data):
    """
    Part 1: Find sum of all invalid IDs in the given ranges.
    
    Args:
        data: Puzzle input data (list of strings or single string)
    
    Returns:
        Sum of all invalid product IDs
    """
    # Parse the input - it's a single line with comma-separated ranges
    if isinstance(data, list):
        input_str = ''.join(data).strip()
    else:
        input_str = data.strip()
    
    # Split by commas to get individual ranges
    ranges = input_str.split(',')
    
    total_sum = 0
    
    for range_str in ranges:
        range_str = range_str.strip()
        if not range_str:
            continue
        
        # Parse the range "start-end"
        parts = range_str.split('-')
        start = int(parts[0])
        end = int(parts[1])
        
        # Check each ID in the range
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total_sum += num
    
    return total_sum


def solve_part2(data):
    """
    Part 2: Find sum of all invalid IDs where a sequence is repeated at least twice.
    
    Args:
        data: Puzzle input data (list of strings or single string)
    
    Returns:
        Sum of all invalid product IDs (repeated at least twice)
    """
    # Parse the input - it's a single line with comma-separated ranges
    if isinstance(data, list):
        input_str = ''.join(data).strip()
    else:
        input_str = data.strip()
    
    # Split by commas to get individual ranges
    ranges = input_str.split(',')
    
    total_sum = 0
    
    for range_str in ranges:
        range_str = range_str.strip()
        if not range_str:
            continue
        
        # Parse the range "start-end"
        parts = range_str.split('-')
        start = int(parts[0])
        end = int(parts[1])
        
        # Check each ID in the range
        for num in range(start, end + 1):
            if is_invalid_id_part2(num):
                total_sum += num
    
    return total_sum


def main():
    """Main entry point for Day 2 solution."""
    # Example test data
    example_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
    
    # Test with example
    print("=== Day 2: Gift Shop ===\n")
    
    if example_data:
        print("Testing with example:")
        example_part1 = solve_part1(example_data)
        print(f"  Part 1: {example_part1} (expected: 1227775554)")
        
        example_part2 = solve_part2(example_data)
        print(f"  Part 2: {example_part2} (expected: 4174379265)")
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
