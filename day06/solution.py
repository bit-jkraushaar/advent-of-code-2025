"""
Advent of Code 2025 - Day 6: Trash Compactor

You're in a garbage smasher with magnetically sealed doors. While waiting for 
cephalopods to open it, you help with math homework.

The math worksheet has problems arranged horizontally - each problem's numbers 
are stacked vertically with the operator at the bottom. Problems are separated 
by full columns of spaces.
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def solve_part1(data):
    """
    Part 1: Calculate the grand total of all problems on the worksheet.
    
    Parse the horizontally arranged worksheet where each column is a problem.
    Problems have numbers stacked vertically with operator at bottom.
    Empty columns separate problems.
    
    Args:
        data: Puzzle input data (list of lines)
    
    Returns:
        Grand total of all problem answers
    """
    if not data:
        return 0
    
    # Find the width of the worksheet
    max_width = max(len(line) for line in data)
    
    # Pad all lines to the same width
    padded_lines = [line.ljust(max_width) for line in data]
    
    # Group columns into problems
    # A problem is a contiguous group of non-empty columns
    # Problems are separated by columns that are entirely spaces
    
    problems = []
    current_problem_start = None
    
    for col_idx in range(max_width):
        # Check if this column is entirely spaces
        column = ''.join(padded_lines[row_idx][col_idx] for row_idx in range(len(padded_lines)))
        is_empty = column.strip() == ''
        
        if is_empty:
            # If we were in a problem, end it
            if current_problem_start is not None:
                problems.append((current_problem_start, col_idx))
                current_problem_start = None
        else:
            # If we're not in a problem, start one
            if current_problem_start is None:
                current_problem_start = col_idx
    
    # Don't forget the last problem
    if current_problem_start is not None:
        problems.append((current_problem_start, max_width))
    
    # Now parse each problem
    grand_total = 0
    
    for start_col, end_col in problems:
        # Extract this problem's text
        problem_lines = []
        for row in padded_lines:
            problem_lines.append(row[start_col:end_col])
        
        # Parse numbers and operator
        # The last line contains the operator
        operator_line = problem_lines[-1].strip()
        operator = operator_line if operator_line in ['+', '*'] else None
        
        # The other lines contain numbers
        numbers = []
        for line in problem_lines[:-1]:
            num_str = line.strip()
            if num_str:
                numbers.append(int(num_str))
        
        # Calculate the result
        if operator and numbers:
            result = numbers[0]
            for num in numbers[1:]:
                if operator == '+':
                    result += num
                elif operator == '*':
                    result *= num
            grand_total += result
    
    return grand_total


def solve_part2(data):
    """
    Part 2: Calculate grand total using cephalopod math (right-to-left columns).
    
    In cephalopod math, numbers are written right-to-left in columns.
    Each column within a problem represents a digit position of the numbers.
    The most significant digit is at the top, least significant at the bottom.
    
    Args:
        data: Puzzle input data
    
    Returns:
        Grand total of all problem answers
    """
    if not data:
        return 0
    
    # Find the width of the worksheet
    max_width = max(len(line) for line in data)
    
    # Pad all lines to the same width
    padded_lines = [line.ljust(max_width) for line in data]
    
    # Group columns into problems (same as part 1)
    problems = []
    current_problem_start = None
    
    for col_idx in range(max_width):
        # Check if this column is entirely spaces
        column = ''.join(padded_lines[row_idx][col_idx] for row_idx in range(len(padded_lines)))
        is_empty = column.strip() == ''
        
        if is_empty:
            # If we were in a problem, end it
            if current_problem_start is not None:
                problems.append((current_problem_start, col_idx))
                current_problem_start = None
        else:
            # If we're not in a problem, start one
            if current_problem_start is None:
                current_problem_start = col_idx
    
    # Don't forget the last problem
    if current_problem_start is not None:
        problems.append((current_problem_start, max_width))
    
    # Now parse each problem using cephalopod math
    grand_total = 0
    
    for start_col, end_col in problems:
        # Extract columns for this problem
        problem_width = end_col - start_col
        
        # Get operator from last row
        operator_line = padded_lines[-1][start_col:end_col].strip()
        operator = operator_line if operator_line in ['+', '*'] else None
        
        if not operator:
            continue
        
        # For each column in the problem, read digits top-to-bottom to form numbers
        # Columns represent digit positions, read right-to-left
        numbers = []
        
        for col_offset in range(problem_width - 1, -1, -1):  # Right to left
            col_idx = start_col + col_offset
            # Read digits from top to bottom (excluding last row which has operator)
            digits = []
            for row_idx in range(len(padded_lines) - 1):
                char = padded_lines[row_idx][col_idx]
                if char.isdigit():
                    digits.append(char)
            
            # Form number from these digits
            if digits:
                number = int(''.join(digits))
                numbers.append(number)
        
        # Calculate the result
        if operator and numbers:
            result = numbers[0]
            for num in numbers[1:]:
                if operator == '+':
                    result += num
                elif operator == '*':
                    result *= num
            grand_total += result
    
    return grand_total


def main():
    """Main entry point for Day 6 solution."""
    # Example test data
    example_data = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  "
    ]
    
    # Test with example
    print("=== Day 6: Trash Compactor ===\n")
    
    if example_data:
        print("Testing with example:")
        example_part1 = solve_part1(example_data)
        print(f"  Part 1: {example_part1} (expected: 4277556)")
        
        example_part2 = solve_part2(example_data)
        print(f"  Part 2: {example_part2} (expected: 3263827)")
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
