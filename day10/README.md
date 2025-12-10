# Day 10: Factory

## Part 1

Configure indicator lights on factory machines by pressing buttons that toggle specific lights.
Find the minimum number of button presses needed to configure all machines.

**Approach**: Linear algebra over GF(2). Try all combinations of buttons starting from smallest sets.
For each combination, simulate pressing those buttons (XOR operation). Return first combination that achieves target.

## Part 2

Configure joltage counters on factory machines by pressing buttons that increment specific counters.
Find the minimum number of button presses needed to reach exact joltage targets for all machines.

**Approach**: Integer Linear Programming (ILP) with PuLP library.
- Each button can be pressed 0 or more times (unlike Part 1's binary toggles)
- Need to minimize total button presses subject to constraints
- Each counter must reach exactly its target value
- Formulate as: minimize sum(button_presses) subject to Ax = b where:
  - A[i][j] = 1 if button j affects counter i
  - x = button press counts (integers ≥ 0)
  - b = target joltage values

**Key Insight**: This is a classic ILP problem that PuLP/CBC solver handles optimally and efficiently.

## Notes

### Part 1: GF(2) Binary Toggles
- This is essentially solving systems of linear equations over the binary field GF(2)
- Pressing a button twice has no effect (toggle twice = no change)
- Only need to determine which buttons to press once (0 or 1 times each)
- Order doesn't matter - button presses are commutative
- Brute force combinatorial search works because button count is typically small

### Part 2: Integer Linear Programming
- **DO NOT** try to solve with pure algorithmic approaches (BFS, DFS, Gaussian elimination)
- Gaussian elimination finds *a* solution but not necessarily the *minimum*
- BFS state-space search is too slow (exponential state space with max joltage ~260)
- Use specialized ILP solver: **PuLP with CBC backend**
- Performance optimizations:
  - Precompute sparse constraint matrix structure
  - Use short variable names to reduce overhead
  - Minimize constraint object creation
- Achieves ~4.6 seconds for 153 machines (under 5-second target)

### Lessons Learned
- When a problem looks like optimization with constraints → consider ILP
- Don't reinvent optimization algorithms - use proven libraries (PuLP, scipy, CVXPY)
- For AoC: if brute force seems too slow, problem likely has mathematical structure
- Reddit community is invaluable for recognizing problem patterns
