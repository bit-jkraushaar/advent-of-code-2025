# Advent of Code 2025 - Quick Reference

## Daily Workflow

### Starting a New Day

1. **Create the day structure:**
   ```bash
   python new_day.py <day_number>
   ```
   This creates:
   - `day<XX>/solution.py` - Template solution file
   - `day<XX>/input.txt` - Empty input file
   - `day<XX>/README.md` - Template README

2. **Add your puzzle input:**
   - Go to https://adventofcode.com/2025/day/X
   - Copy your personal input
   - Paste into `day<XX>/input.txt`

3. **Implement the solution:**
   - Edit `day<XX>/solution.py`
   - Fill in the `solve_part1()` function
   - Add example data and expected results
   - Test with example first

4. **Run and test:**
   ```bash
   python run.py <day_number>
   ```

5. **When Part 2 is released:**
   - Implement `solve_part2()` function
   - Uncomment Part 2 code in `main()`
   - Run again to get both answers

## Commands

| Command | Description |
|---------|-------------|
| `python new_day.py 2` | Create day 2 structure |
| `python run.py 1` | Run day 1 solution |
| `python run.py all` | Run all completed solutions |
| `python day01/solution.py` | Run day 1 directly |
| `python test_all.py` | Test all solutions (no output) |
| `pip install -r requirements.txt` | Install external dependencies (if needed) |

## Project Structure

```
advent-of-code/
├── run.py              # Main runner (run specific or all days)
├── new_day.py          # Create new day directories
├── template.py         # Template for new solutions
├── test_all.py         # Test all solutions
├── requirements.txt    # External dependencies (e.g., PuLP for ILP)
├── utils/              # Shared utilities
│   ├── __init__.py
│   └── input_reader.py # File reading helpers
├── day01/              # Each day in its own folder
│   ├── solution.py     # Solution implementation
│   ├── input.txt       # Your puzzle input
│   └── README.md       # Notes and explanations
└── .gitignore

```

## Utility Functions

Available from `utils.input_reader`:

```python
from utils.input_reader import read_input

# Read non-empty lines (most common)
lines = read_input('input.txt')  # ['line1', 'line2', ...]

# Read raw content
content = read_input_raw('input.txt')  # 'full file content...'

# Read all lines including empty ones
all_lines = read_input_lines('input.txt')  # ['line1', '', 'line3', ...]

# Read groups separated by blank lines
groups = read_input_groups('input.txt')  # [['group1line1', 'group1line2'], ['group2line1'], ...]
```

## Solution Template Structure

Each solution follows this pattern:

```python
def solve_part1(data):
    """Solve part 1"""
    # Your solution here
    return result

def solve_part2(data):
    """Solve part 2"""
    # Your solution here
    return result

def main():
    """Main entry point"""
    # Test with example
    example_data = [...]
    example_result = solve_part1(example_data)
    print(f"Example: {example_result}")
    
    # Solve actual puzzle
    data = read_input('input.txt')
    answer = solve_part1(data)
    print(f"Part 1: {answer}")
```

## Tips

- **Always test with the example first** before running on actual input
- **Keep Part 1 working** when implementing Part 2
- **Document your approach** in the day's README.md
- **Use the utilities** to avoid repeating file reading code
- **Run `test_all.py`** before committing to ensure nothing broke
- **Install dependencies** with `pip install -r requirements.txt` when needed
- **Recognize problem patterns** - some puzzles require specialized libraries (ILP, graphs, etc.)

## Git Workflow (Optional)

```bash
# Don't commit input files (they're personal)
git add day01/solution.py day01/README.md
git commit -m "Add day 1 solution"

# Or commit everything except inputs
git add .
git reset day*/input.txt
git commit -m "Add day 1 solution"
```

## File Organization

- **Keep each day independent** - solutions should run standalone
- **Use utils for shared code** - don't duplicate common functions
- **Document interesting solutions** - update day's README.md with notes
- **Track progress** - update main README.md progress table

## Example Session

```bash
# December 2nd morning
$ python new_day.py 2
Created directory: day02/
Created solution file: day02/solution.py
...

# Copy puzzle input to day02/input.txt
# Edit day02/solution.py and implement solve_part1()

$ python run.py 2
=== Day 2: [Title] ===
Testing with example:
  Part 1: 42 (expected: 42)
Puzzle answers:
  Part 1: 12345

# Later, when Part 2 is released
# Edit day02/solution.py and implement solve_part2()

$ python run.py 2
=== Day 2: [Title] ===
Testing with example:
  Part 1: 42 (expected: 42)
  Part 2: 84 (expected: 84)
Puzzle answers:
  Part 1: 12345
  Part 2: 67890
```

Happy coding! 🎄
