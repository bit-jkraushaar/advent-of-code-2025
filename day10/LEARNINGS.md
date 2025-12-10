# Day 10 - Key Learnings and Documentation

## Problem Summary

**Day 10: Factory** - Two-part puzzle involving factory machine configuration

### Part 1: Toggle Lights (GF(2))
- Configure indicator lights by pressing buttons that toggle specific lights
- Each button affects a subset of lights (XOR operation)
- Each button pressed at most once (0 or 1 times)
- Find minimum button presses to reach target light pattern

**Solution**: Combinatorial search over GF(2) binary field
- Try all combinations starting from smallest sets
- Simulate button presses with XOR operations
- Return first combination that achieves target

### Part 2: Joltage Counters (Integer Linear Programming)
- Configure joltage counters by pressing buttons that increment specific counters
- Each button can be pressed 0 or more times (unlimited)
- Each button affects a subset of counters (+1 to each)
- Find minimum total button presses to reach exact target values

**Solution**: Integer Linear Programming with PuLP

## Critical Insights

### 1. Problem Recognition
When you see a problem asking to:
- **Minimize/maximize** a sum of variables
- Subject to **linear constraints** (equalities or inequalities)
- With **integer** or binary variables

→ **This is an ILP/LP problem** - use specialized solvers, not algorithmic search!

### 2. Failed Approaches (What NOT to Do)

❌ **BFS State-Space Search**
- Tried exploring state space from [0,0,...] to target
- Problem: Exponential state explosion
- With max joltage ~260 and ~7 counters, too many states
- Result: Too slow (>5 seconds)

❌ **Gaussian Elimination**
- Tried solving system of linear equations directly
- Problem: Finds *a* solution, not the *minimum*
- For underdetermined systems (more buttons than counters), infinite solutions exist
- Setting free variables to 0 gives one answer, but not optimal
- Result: Fast (0.3s) but incorrect (8093 vs 15132)

❌ **Combination Search with Gaussian**
- Tried all subsets of buttons, solve with Gaussian for each
- Problem: Still doesn't guarantee minimum across all subsets
- Result: Still incorrect (7523 vs 15132)

### 3. Correct Approach: Integer Linear Programming

✅ **PuLP with CBC Solver**

**Formulation:**
```
Minimize: sum(x_i) for all button variables x_i

Subject to:
  For each counter j:
    sum(x_i for i in buttons_affecting_counter_j) = target_j
  
  All x_i >= 0 and integer
```

**Why it works:**
- CBC (COIN-OR Branch and Cut) is a proven ILP solver
- Uses simplex method + branch-and-bound for integer constraints
- Guaranteed to find global optimum
- Highly optimized C++ implementation

**Implementation:**
```python
import pulp

prob = pulp.LpProblem("Joltage", pulp.LpMinimize)

# Variables: button press counts
button_vars = [pulp.LpVariable(f"b{i}", 0, None, 'Integer') 
               for i in range(len(buttons))]

# Objective: minimize total presses
prob += pulp.lpSum(button_vars)

# Constraints: each counter reaches target
for counter_idx in range(len(joltage)):
    prob += (
        pulp.lpSum(button_vars[btn_idx] 
                  for btn_idx, button in enumerate(buttons) 
                  if counter_idx in button) 
        == joltage[counter_idx]
    )

prob.solve(pulp.PULP_CBC_CMD(msg=0))
return int(pulp.value(prob.objective))
```

### 4. Performance Optimizations

**Initial PuLP implementation: 8.2 seconds** (too slow)

Optimizations applied:
1. **Precompute sparse constraint matrix**
   - Build list of which buttons affect each counter once
   - Avoid repeated `if counter_idx in button` checks
   
2. **Use shorter variable names**
   - `f"b{i}"` instead of longer descriptive names
   - Reduces string overhead in constraint building
   
3. **Minimize constraint object creation**
   - Use list comprehensions efficiently
   - Build lpSum directly without intermediate lists

**Final performance: 4.64 seconds** (under 5-second target) ✓

### 5. Example Validation

Critical to test on provided examples:
```
Machine 1: [.##.] {3,5,4,7} → 10 presses (not 12)
Machine 2: [...#.] {7,5,12,7,2} → 13 presses  
Machine 3: [.###.#] {10,11,11,5,10,5} → 10 presses
Total: 33 presses
```

Examples helped identify that:
- Gaussian elimination was giving 22 (wrong)
- Combination approach was giving 12 (wrong)
- PuLP ILP solver gave 33 (correct) ✓

### 6. Reddit Community Value

Found solution pattern through Reddit thread:
- https://www.reddit.com/r/adventofcode/comments/1pivlyh/
- Community consensus: "This is an ILP problem"
- Confirmed PuLP library is the right tool
- Multiple successful solvers using same approach

**Lesson**: When stuck, check Reddit r/adventofcode - pattern recognition from experienced solvers

## Dependencies

Added to `requirements.txt`:
```
# Day 10 Part 2: Integer Linear Programming solver
pulp>=2.7.0
```

Install with:
```bash
pip install -r requirements.txt
```

## Final Results

- **Part 1**: 434 (combinatorial search, <0.1s)
- **Part 2**: 15132 (PuLP ILP solver, 4.64s)
- **Total runtime**: 4.85 seconds ✓
- **Examples validated**: 7 and 33 ✓

## Key Takeaways

1. **Recognize optimization patterns** - ILP, shortest path, MST, etc.
2. **Use specialized libraries** - Don't reinvent the wheel
3. **Test examples first** - They reveal algorithmic issues early
4. **Community is valuable** - Reddit helps with pattern recognition
5. **Performance matters** - Optimize constraint building for ILP
6. **Document learnings** - Future puzzles may have similar patterns

## References

- PuLP Documentation: https://coin-or.github.io/pulp/
- CBC Solver: https://github.com/coin-or/Cbc
- AoC 2025 Day 10: https://adventofcode.com/2025/day/10
- Reddit Discussion: https://www.reddit.com/r/adventofcode/comments/1pivlyh/
