# Day 12: Christmas Tree Farm

## Part 1

Polyomino packing problem - determine how many rectangular regions can fit all their required present shapes. Presents are 7-cell polyominoes that can be rotated and flipped.

## Part 2

[Description of part 2]

## Notes

**Solution Approach:**
- Used Google OR-Tools CP-SAT solver for constraint satisfaction
- Critical optimization: Filter regions where total cells needed > available area (reduced 1000 → 414 regions)
- Hybrid strategy:
  - Small problems (≤80 presents): Exact CP-SAT solving
  - Large problems (>80 presents): Slack-based heuristic (~15% extra space required)
- Limited placements to 200 per present to prevent memory issues
- Answer: 414 regions can fit all their presents
