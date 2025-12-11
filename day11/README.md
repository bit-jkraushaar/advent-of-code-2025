# Day 11: Reactor

## Part 1

Count all paths from device 'you' to device 'out' through a graph of connected devices.

Used dynamic programming with path counting:
- Build graph from device connections
- Use BFS to get topological ordering
- Accumulate path counts at each node from predecessors
- Avoids exponential enumeration by counting paths instead of tracking them

## Part 2

Count paths from 'svr' to 'out' that visit both 'dac' and 'fft' devices (in any order).

Key optimization: Use DP with state `(node, has_visited_dac, has_visited_fft)`
- Critical: Don't include visited set in memoization key
- Assumes DAG structure (no cycles causing infinite paths)
- State space is O(nodes × 2 × 2) = O(4n) instead of exponential
- Memoize count of paths from each state to target

## Notes

**Performance lesson**: When counting paths with constraints in a DAG:
- ❌ BAD: Include full visited set in state → exponential complexity
- ✅ GOOD: Only memoize on (node, constraint_flags) → polynomial complexity

Similar to Day 7's optimization: count paths, don't enumerate them.
