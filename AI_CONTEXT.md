# Advent of Code 2025 - AI Assistant Context

## Project Overview

This is an Advent of Code 2025 solution repository using Python. The project is structured to make it easy to add new days' solutions while maintaining consistency and reusability.

## Project Structure

```
advent-of-code/
├── run.py              # Main runner script
├── new_day.py          # Script to create new day directories
├── template.py         # Template for new solutions
├── test_all.py         # Test all solutions
├── README.md           # Project overview
├── GUIDE.md            # User guide
├── .gitignore          # Git ignore
├── utils/              # Shared utilities
│   ├── __init__.py
│   └── input_reader.py # Input reading utilities
└── dayXX/              # Each day's solution
    ├── solution.py     # Solution implementation
    ├── input.txt       # Puzzle input (user's personal input)
    └── README.md       # Day-specific notes
```

## Workflow for Adding New Days

When the user provides a new puzzle, follow these steps:

### 1. Create New Day Structure
```bash
python new_day.py <day_number>
```
This automatically creates:
- `day<XX>/solution.py` (from template)
- `day<XX>/input.txt` (empty)
- `day<XX>/README.md` (template)

### 2. Implement the Solution

Edit `day<XX>/solution.py`:
- Update the docstring with puzzle title and description
- Implement `solve_part1(data)` function
- Add example test data
- Update expected results
- When Part 2 is available, implement `solve_part2(data)`

### 3. Add Puzzle Input

The user will provide their puzzle input. Save it to `day<XX>/input.txt`.

### 4. Update Documentation

- Update `day<XX>/README.md` with puzzle description and notes
- Update main `README.md` progress table

### 5. Test and Run

```bash
python run.py <day_number>  # Run specific day
python test_all.py          # Test all days
```

## Code Standards

### Solution File Structure

Each `solution.py` follows this pattern:

```python
"""
Advent of Code 2025 - Day XX: [Puzzle Title]

[Brief puzzle description]
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def solve_part1(data):
    """
    Part 1: [Description]
    
    Args:
        data: Puzzle input data
    
    Returns:
        Solution for part 1
    """
    # Implementation
    pass


def solve_part2(data):
    """
    Part 2: [Description]
    
    Args:
        data: Puzzle input data
    
    Returns:
        Solution for part 2
    """
    # Implementation
    pass


def main():
    """Main entry point for Day XX solution."""
    # Example test data
    example_data = [
        # Example input
    ]
    
    # Test with example
    print("=== Day XX: [Puzzle Title] ===\n")
    
    if example_data:
        print("Testing with example:")
        example_part1 = solve_part1(example_data)
        print(f"  Part 1: {example_part1} (expected: [EXPECTED])")
        print()
    
    # Solve actual puzzle
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    
    try:
        data = read_input(input_file)
        
        part1_answer = solve_part1(data)
        print("Puzzle answers:")
        print(f"  Part 1: {part1_answer}")
        
        # Uncomment when part 2 is available
        # part2_answer = solve_part2(data)
        # print(f"  Part 2: {part2_answer}")
        
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        print("Please add your puzzle input to solve the actual puzzle.")


if __name__ == "__main__":
    main()
```

### Input Reading Utilities

Available from `utils.input_reader`:

```python
# Most common - read non-empty lines
data = read_input('input.txt')  # Returns: ['line1', 'line2', ...]

# Read raw file content
content = read_input_raw('input.txt')  # Returns: 'full content...'

# Read all lines including empty ones
lines = read_input_lines('input.txt')  # Returns: ['line1', '', 'line3', ...]

# Read groups separated by blank lines
groups = read_input_groups('input.txt')  # Returns: [['group1'], ['group2'], ...]
```

## Common Patterns for Advent of Code

### Grid/Map Problems
```python
grid = [list(line) for line in data]
# or
grid = {(x, y): char for y, line in enumerate(data) 
        for x, char in enumerate(line)}
```

### Number Parsing
```python
numbers = [int(x) for x in data]
# or from comma-separated
numbers = [int(x) for x in data[0].split(',')]
```

### Graph/Path Problems
```python
from collections import deque, defaultdict

graph = defaultdict(list)
for line in data:
    # Parse connections
    graph[node].append(neighbor)
```

## Completed Days

### Day 1: Secret Entrance
- **Theme**: Circular dial with rotations
- **Part 1**: Count times dial ends on 0 after rotations
- **Part 2**: Count all times dial passes through 0 during rotations
- **Key Concept**: Modular arithmetic, counting during vs after operations
- **Solutions**: Part 1: 982, Part 2: 6106

### Day 5: Cafeteria
- **Theme**: Ingredient inventory management with ID ranges
- **Part 1**: Count how many available IDs fall within fresh ranges
- **Part 2**: Count total unique IDs covered by all fresh ranges
- **Key Concept**: Range merging optimization - avoid iterating millions of individual values
- **Solutions**: Part 1: 529, Part 2: 344260049617193
- **Important Lesson**: Use range arithmetic instead of sets for large ranges

### Day 6: Trash Compactor
- **Theme**: Cephalopod math worksheet parsing
- **Part 1**: Parse horizontally arranged math problems (traditional left-to-right reading)
- **Part 2**: Parse using cephalopod math (right-to-left column reading where each column is a digit position)
- **Key Concept**: Different parsing strategies for the same input format
- **Solutions**: Part 1: 5667835681547, Part 2: 9434900032651
- **Important Lesson**: Column-wise vs row-wise data interpretation

## Important Notes for AI Assistant

1. **Always test with examples first** - Each puzzle provides examples with expected results
2. **Keep Part 1 working** - When implementing Part 2, don't break Part 1
3. **Use the utilities** - Don't rewrite file reading code
4. **Follow the template** - Maintain consistency across days
5. **Document the approach** - Update README.md with solution explanation
6. **Parse input correctly** - AoC input format varies (lines, grids, numbers, etc.)
7. **Watch for edge cases** - Examples often don't cover all cases
8. **Optimize if needed** - Part 2 often requires optimization of Part 1 approach

## Typical User Workflow

1. User will paste the puzzle description
2. User may provide example input and expected output
3. User will have already added their personal input to `dayXX/input.txt` (or will add it)
4. Implement the solution
5. Test with example
6. Run on actual input
7. When Part 2 is released, add it to the same solution file

## Python Environment

- Python 3.13.9 in virtual environment
- Location: `C:/dev/advent-of-code/.venv/Scripts/python.exe`
- No external dependencies required (use standard library)
- If needed, add dependencies and document them

## Running Solutions

```bash
# Run specific day
C:/dev/advent-of-code/.venv/Scripts/python.exe run.py 1

# Or shorter via script
python run.py 1

# Run all days
python run.py all

# Run directly
python day01/solution.py

# Test all (no output)
python test_all.py
```

## File Locations

- **User's puzzle input**: Always in `dayXX/input.txt`
- **Solution code**: Always in `dayXX/solution.py`
- **Day notes**: Always in `dayXX/README.md`
- **Shared utilities**: In `utils/` directory
- **Templates**: `template.py` for new solutions

## Common AoC Input Types

1. **List of numbers** (one per line)
2. **Grid/Map** (2D character array)
3. **Instructions** (e.g., "move 3", "rotate left")
4. **Comma-separated values**
5. **Groups separated by blank lines**
6. **Key-value pairs** or structured data
7. **Graph edges** (node-to-node connections)

## Tips for Success

- **Read carefully** - AoC puzzles have subtle requirements
- **Start simple** - Get Part 1 working before optimizing
- **Reuse code** - Part 2 often builds on Part 1
- **Think about scale** - Part 2 often requires handling larger inputs
- **Use appropriate data structures** - Sets, dicts, deques, etc.
- **Don't overthink** - Most solutions are 20-50 lines of code

## Performance and Optimization

### Avoiding Memory/Time Issues with Large Ranges

**CRITICAL**: When working with numeric ranges in AoC puzzles:

- **DO NOT** iterate through every individual value in a range
- **DO NOT** create sets/lists of millions of individual IDs from ranges
- **DO** use range arithmetic and merging algorithms

**Example - Day 5 (Cafeteria):**
- ❌ **BAD**: `for id in range(start, end + 1): fresh_ids.add(id)` → Memory overflow on large ranges
- ✅ **GOOD**: Merge overlapping ranges, then count: `total += (end - start + 1)`

**Range Merging Algorithm:**
```python
# Sort ranges by start position
ranges.sort()

# Merge overlapping or adjacent ranges
merged = []
for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:
        # Extend the last merged range
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        # Add as new range
        merged.append((start, end))

# Count total values in O(n) instead of O(total_values)
total = sum(end - start + 1 for start, end in merged)
```

**Key principle**: Work with range boundaries, not individual values.

## Progress Tracking

Update the main README.md progress table after each day:

```markdown
| Day | Title | Part 1 | Part 2 | Notes |
|-----|-------|--------|--------|-------|
| [01](day01/) | Secret Entrance | ⭐ | ⭐ | Circular dial rotations |
| [02](day02/) | Title | ⭐ | ⭐ | Brief note |
```

## Summary

This project is set up for efficiency and consistency. When a new puzzle arrives:
1. Create the day structure (`python new_day.py X`)
2. Implement the solution in `dayXX/solution.py`
3. Test with examples
4. Run on actual input
5. Document and update progress

The infrastructure handles the rest (file organization, running, testing).
