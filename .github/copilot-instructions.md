# Advent of Code 2025 - AI Coding Agent Instructions

## Project Context

This is an **Advent of Code 2025** solution repository using Python. Most code is AI-generated (GitHub Copilot + Claude Sonnet 4.5) as an experiment in AI problem-solving capabilities. The project prioritizes consistency, testability, and rapid daily puzzle iteration.

## Architecture & Structure

```
advent-of-code/
├── dayXX/solution.py    # Standalone solutions (always follow template.py structure)
├── utils/               # Shared utilities - use these, don't duplicate
├── run.py              # Runner for individual/all days
├── new_day.py          # Scaffolding script - ALWAYS use this for new days
└── template.py         # Sacred template - solutions MUST match this structure
```

**Key principle**: Each day is **completely independent**. Solutions must run standalone (`python dayXX/solution.py`) AND through the runner (`python run.py XX`).

## Critical Workflows

### Adding New Days (MANDATORY PROCESS)

**ALWAYS use the scaffolding script** - never create day directories manually:

```bash
python new_day.py 8
```

This creates the correct structure and pre-fills `solution.py` with the template. Then:

1. **Add puzzle input** to `dayXX/input.txt` (user provides this)
2. **Implement only the functions** - DO NOT modify the template structure:
   - `solve_part1(data)` - implement logic here
   - `solve_part2(data)` - implement when Part 2 released
   - Update `example_data` in `main()` with example from puzzle description
   - Update expected values in print statements
3. **Update `dayXX/README.md`** with puzzle title and notes
4. **Update main `README.md`** progress table

### Running & Testing

```bash
python run.py 7          # Run single day
python run.py all        # Run all days
python day07/solution.py # Direct execution (for debugging)
python test_all.py       # Verify all solutions (silent unless errors)
```

## Code Conventions

### Solution File Structure (IMMUTABLE)

**CRITICAL**: All solutions MUST follow this exact pattern from `template.py`:

```python
"""
Advent of Code 2025 - Day XX: [PUZZLE TITLE]

[Brief puzzle description]
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.input_reader import read_input

def solve_part1(data):
    """Part 1: [Description]"""
    # Implementation here
    pass

def solve_part2(data):
    """Part 2: [Description]"""
    # Implementation here
    pass

def main():
    """Main entry point for Day XX solution."""
    example_data = [...]  # Example from puzzle
    
    print("=== Day XX: [PUZZLE TITLE] ===\n")
    print("Testing with example:")
    example_part1 = solve_part1(example_data)
    print(f"  Part 1: {example_part1} (expected: [EXPECTED])")
    print()
    
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    try:
        data = read_input(input_file)
        part1_answer = solve_part1(data)
        print("Puzzle answers:")
        print(f"  Part 1: {part1_answer}")
        # Uncomment when part 2 available:
        # part2_answer = solve_part2(data)
        # print(f"  Part 2: {part2_answer}")
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")

if __name__ == "__main__":
    main()
```

**Why this structure matters**:
- `sys.path.insert()` pattern enables both standalone AND runner execution
- `main()` structure provides example validation before solving actual puzzle
- Output format consistency across all days
- Part 2 commented out until released (AoC releases parts sequentially)

### Input Reading (Use Utilities)

**ALWAYS use `utils.input_reader`** - never read files manually:

```python
from utils.input_reader import read_input

# Most common - non-empty lines, whitespace stripped
lines = read_input('input.txt')  # ['line1', 'line2']

# Raw content (for special parsing)
content = read_input_raw('input.txt')  # 'full content...'

# All lines including empty (rare)
all_lines = read_input_lines('input.txt')  # ['line1', '', 'line3']

# Groups separated by blank lines (common in AoC)
groups = read_input_groups('input.txt')  # [['group1'], ['group2']]
```

### Common Patterns Library

**Reference `utils/aoc_patterns.py`** before implementing - contains proven snippets for:
- Grid parsing (list vs dict representations)
- Graph traversal (BFS/DFS/Dijkstra with heapq)
- 4-directional/8-directional movement
- Regex number extraction
- Counter/defaultdict patterns

**Example**: Grid problems - use the dict pattern for sparse grids, list pattern for dense grids:

```python
# Dense grid (most common)
grid = [list(line) for line in data]
grid[row][col]  # Access

# Sparse grid or need (x,y) lookups
grid = {(x, y): char 
        for y, line in enumerate(data)
        for x, char in enumerate(line)}
```

## Testing Philosophy

1. **Always test examples first** - AoC provides examples with expected outputs
2. **Add example data to `main()`** - validates logic before running on large inputs
3. **Keep Part 1 working** when implementing Part 2 (parts are cumulative)
4. **Use `test_all.py`** before committing to catch regressions
5. **Performance requirement** - Solutions should complete in **under 10 seconds**
   - If a solution exceeds 10 seconds, optimize or consider alternative algorithms
   - For optimization problems (minimize/maximize with constraints), consider specialized libraries:
     - Integer Linear Programming: PuLP, scipy.optimize
     - Graph algorithms: networkx
     - Don't reinvent the wheel - use proven mathematical solvers

## Integration Points

- **Minimal external dependencies** - prefer stdlib when possible
- **Specialized libraries allowed** - when problem requires (ILP, graphs, etc.)
  - Add dependencies to `requirements.txt` with comments explaining which day uses them
  - Example: `pulp>=2.7.0  # Day 10 Part 2: Integer Linear Programming`
- **Python 3.9+** - uses modern features (walrus operator, dict merge, etc.)
- **Git ignores `input.txt`** files - they're personal puzzle inputs (not shareable)

## Key Files for Context

- `AI_CONTEXT.md` - Full project overview for AI assistants
- `utils/aoc_patterns.py` - Copy-paste reference for common algorithms
- `template.py` - The authoritative solution structure

## Common Mistakes to Avoid

1. ❌ Creating day directories manually → ✅ Use `python new_day.py XX`
2. ❌ Modifying template structure → ✅ Only implement `solve_part1/2` functions
3. ❌ Reading files manually → ✅ Use `utils.input_reader` functions
4. ❌ Running untested code → ✅ Add example data and validate first
5. ❌ Breaking Part 1 when adding Part 2 → ✅ Keep both working
6. ❌ Forgetting to update README progress table → ✅ Update after solving

## Development Flow Example

```bash
# December 8th, new puzzle released
python new_day.py 8
# Add input.txt content from adventofcode.com
# Edit day08/solution.py - implement solve_part1()
python run.py 8  # Test example + solve
# Submit Part 1 answer

# Part 2 released later
# Edit day08/solution.py - implement solve_part2()
# Uncomment Part 2 code in main()
python run.py 8  # Verify Part 1 still works, solve Part 2
# Submit Part 2 answer

# Update main README.md progress table
python test_all.py  # Verify no regressions
git add day08/solution.py day08/README.md README.md
git commit -m "Add day 8 solution"
```
