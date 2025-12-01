# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) implemented in Python.

## Project Structure

```
advent-of-code/
├── run.py              # Main runner script
├── new_day.py          # Script to create new day directories
├── template.py         # Template for new solutions
├── utils/              # Shared utility functions
│   └── input_reader.py # Input file reading utilities
├── day01/              # Day 1 solution
│   ├── solution.py     # Solution implementation
│   ├── input.txt       # Puzzle input
│   └── README.md       # Day-specific notes
├── day02/              # Day 2 solution
│   └── ...
└── ...
```

## Quick Start

### Running Solutions

Run a specific day:
```bash
python run.py 1
```

Run all completed days:
```bash
python run.py all
```

Or run a day's solution directly:
```bash
python day01/solution.py
```

### Creating a New Day

Use the helper script to set up a new day:
```bash
python new_day.py 2
```

This will:
- Create a `day02/` directory
- Copy the template to `solution.py`
- Create empty `input.txt` and `README.md` files

Then:
1. Add your puzzle input to `dayXX/input.txt`
2. Implement your solution in `dayXX/solution.py`
3. Run with `python run.py XX`

## Utilities

The `utils/` directory contains shared helper functions:

- `read_input(filename)` - Read non-empty lines from a file
- `read_input_raw(filename)` - Read raw file content
- `read_input_lines(filename)` - Read all lines including empty ones
- `read_input_groups(filename)` - Read input separated by blank lines

## Progress

| Day | Title | Part 1 | Part 2 | Notes |
|-----|-------|--------|--------|-------|
| [01](day01/) | Secret Entrance | ⭐ | ⭐ | Circular dial rotations |

## Notes

Each day's directory contains:
- `solution.py` - The solution implementation
- `input.txt` - Your personal puzzle input
- `README.md` - Notes and observations about the puzzle

## Reference Documentation

- **[QUICK_START.md](QUICK_START.md)** - Quick reference for adding new days
- **[GUIDE.md](GUIDE.md)** - Comprehensive usage guide
- **[AI_CONTEXT.md](AI_CONTEXT.md)** - Full project context for AI assistance
- **[utils/aoc_patterns.py](utils/aoc_patterns.py)** - Common code patterns and snippets
