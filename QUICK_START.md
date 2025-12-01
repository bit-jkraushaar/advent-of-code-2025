# Quick Start for New Days

## When User Provides New Puzzle

### Step 1: Create Day Structure
```bash
python new_day.py <day_number>
```

### Step 2: Add Input
User will provide their puzzle input → save to `day<XX>/input.txt`

### Step 3: Implement Solution

1. Open `day<XX>/solution.py`
2. Update docstring with puzzle title
3. Parse the example from puzzle description
4. Add example data to `main()` function
5. Implement `solve_part1(data)` 
6. Test with example first
7. Run on actual input
8. When Part 2 arrives, implement `solve_part2(data)`

### Step 4: Document
- Update `day<XX>/README.md` with approach/notes
- Update main `README.md` progress table

## Key Files to Reference

- **AI_CONTEXT.md** - Full context about project structure and patterns
- **utils/aoc_patterns.py** - Common code snippets and patterns
- **template.py** - Template structure for new solutions
- **GUIDE.md** - User workflow guide

## Common Input Patterns

1. **Lines of text** → `read_input('input.txt')`
2. **Numbers** → `[int(x) for x in read_input('input.txt')]`
3. **Grid** → `[list(line) for line in read_input('input.txt')]`
4. **Groups** → `read_input_groups('input.txt')`

## Running Solutions

```bash
python run.py <day>     # Run specific day
python run.py all       # Run all days
python test_all.py      # Test all (silent)
```

## Remember

- ✅ Test with examples first
- ✅ Keep Part 1 working when adding Part 2
- ✅ Use utilities from `utils/`
- ✅ Follow the template structure
- ✅ Document interesting solutions
