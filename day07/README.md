# Day 7: Laboratories

## Part 1

Count how many times a tachyon beam is split as it propagates through a manifold.

A tachyon beam enters at location 'S' and moves downward. When it encounters a splitter ('^'), the beam stops and creates two new beams from the immediate left and right positions of the splitter. These new beams also move downward and can trigger additional splits.

### Solution Approach

1. All beams move downward through the manifold
2. When a beam hits a splitter ('^'):
   - The current beam stops
   - Two new beams are created at positions immediately left and right of the splitter
   - These new beams continue moving downward
3. Use BFS to track all active beams and count splits
4. Track visited positions to avoid infinite loops

### Key Insights

- ALL beams only move downward (not horizontally)
- When a splitter is hit, the split creates beams offset left/right but they continue downward
- Each split event counts once
- Beams can exit the manifold by going out of bounds

## Part 2

Count the number of timelines using the many-worlds interpretation of quantum tachyon splitting.

In a quantum tachyon manifold, a single particle takes BOTH paths at each splitter, creating parallel timelines. Count the total number of distinct timelines (paths) that result.

### Solution Approach

1. Use dynamic programming with path counting instead of tracking individual paths
2. Track how many distinct paths reach each position (not the paths themselves)
3. When paths hit a splitter, the count at that position splits between left and right
4. Sum all path counts for positions that exit the manifold

### Key Insights

- **Critical Optimization**: Track path counts, not individual paths
- When n paths reach a splitter, n paths go left and n paths go right
- Path counts accumulate at each position
- This avoids exponential path explosion: O(positions) instead of O(2^splits)

### Performance

- Naive approach: Track every path individually → exponential time/memory
- Optimized approach: Count paths at each position → linear in grid size
- Example: 21 splits → 40 timelines (not 2^21 = 2M+)

## Notes

**Part 1**: Simple BFS simulation counting split events (Answer: 1649)

**Part 2**: Dynamic programming path counting (Answer: 16937871060075)

The key lesson is recognizing when to count paths instead of enumerating them. This is a common optimization pattern in AoC puzzles.
