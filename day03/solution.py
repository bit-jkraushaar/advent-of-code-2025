"""
Advent of Code 2025 - Day 3: Lobby

You need to power the escalator using batteries. Each line represents a bank of batteries
with joltage ratings (digits 1-9). You must turn on exactly 2 batteries per bank to produce
a joltage equal to the 2-digit number formed. Find the maximum joltage possible from each
bank and sum them.
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def solve_part1(data):
    """
    Part 1: Find maximum joltage from each battery bank
    
    For each bank (line), find the largest 2-digit number that can be formed
    by selecting exactly 2 batteries in their original order.
    
    Args:
        data: List of strings, each representing a bank of batteries
    
    Returns:
        Total output joltage (sum of max joltage from each bank)
    """
    total_joltage = 0
    
    for bank in data:
        bank = bank.strip()
        if not bank:
            continue
            
        max_joltage = 0
        
        # Try all pairs of positions (i, j) where i < j
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                # Form a 2-digit number from positions i and j
                joltage = int(bank[i] + bank[j])
                max_joltage = max(max_joltage, joltage)
        
        total_joltage += max_joltage
    
    return total_joltage


def solve_part2(data):
    """
    Part 2: Find maximum joltage by selecting exactly 12 batteries
    
    For each bank (line), find the largest 12-digit number that can be formed
    by selecting exactly 12 batteries in their original order.
    
    Strategy: To maximize the number, we want to keep the largest digits.
    We'll remove the smallest digits (or smallest contributing digits) while
    maintaining order.
    
    Args:
        data: List of strings, each representing a bank of batteries
    
    Returns:
        Total output joltage (sum of max joltage from each bank)
    """
    total_joltage = 0
    
    for bank in data:
        bank = bank.strip()
        if not bank:
            continue
        
        # We need to select 12 batteries from the bank
        # To maximize, we want to keep the 12 batteries that form the largest number
        # This is equivalent to removing (len(bank) - 12) batteries to minimize the result
        
        n = len(bank)
        to_remove = n - 12
        
        if to_remove <= 0:
            # If bank has 12 or fewer batteries, use all of them
            max_joltage = int(bank)
        else:
            # Use a greedy approach: repeatedly remove the digit that,
            # when removed, leaves the largest remaining number
            # This is like finding the maximum by removing smallest "blocking" digits
            
            # Convert to list for easier manipulation
            digits = list(bank)
            
            # Remove to_remove digits
            for _ in range(to_remove):
                # Find the position to remove:
                # We want to remove the first digit that is smaller than the next digit
                # If no such digit exists, remove the last digit
                removed = False
                for i in range(len(digits) - 1):
                    if digits[i] < digits[i + 1]:
                        digits.pop(i)
                        removed = True
                        break
                
                if not removed:
                    # All digits are in descending order, remove the last one
                    digits.pop()
            
            max_joltage = int(''.join(digits))
        
        total_joltage += max_joltage
    
    return total_joltage


def main():
    """Main entry point for Day 3 solution."""
    # Example test data
    example_data = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]
    
    # Test with example
    print("=== Day 3: Lobby ===\n")
    
    if example_data:
        print("Testing with example:")
        example_part1 = solve_part1(example_data)
        print(f"  Part 1: {example_part1} (expected: 357)")
        
        example_part2 = solve_part2(example_data)
        print(f"  Part 2: {example_part2} (expected: 3121910778619)")
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
