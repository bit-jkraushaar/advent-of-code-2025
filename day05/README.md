# Day 5: Cafeteria

## Part 1

Determine how many available ingredient IDs are fresh based on fresh ID ranges.

The database consists of:
1. Fresh ID ranges (e.g., "3-5" means IDs 3, 4, and 5 are fresh)
2. A blank line separator
3. Available ingredient IDs to check

Rules:
- Fresh ID ranges are inclusive
- Ranges can overlap (an ID is fresh if it's in ANY range)
- Count how many available IDs fall within at least one fresh range

### Example
```
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

Results:
- ID 1: spoiled (not in any range)
- ID 5: fresh (in range 3-5)
- ID 8: spoiled
- ID 11: fresh (in range 10-14)
- ID 17: fresh (in ranges 16-20 and 12-18)
- ID 32: spoiled

Answer: **3** fresh ingredients

## Part 2

Find the total count of all ingredient IDs that are considered fresh by the fresh ID ranges.

For Part 2, the available ingredient IDs section is irrelevant. We need to determine how many unique ingredient IDs are covered by ALL the fresh ranges combined.

### Example
Using the same fresh ranges:
```
3-5      → covers IDs: 3, 4, 5
10-14    → covers IDs: 10, 11, 12, 13, 14
16-20    → covers IDs: 16, 17, 18, 19, 20
12-18    → covers IDs: 12, 13, 14, 15, 16, 17, 18
```

Combining all ranges (with overlaps removed):
- 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

Answer: **14** unique ingredient IDs are considered fresh

### Solution Approach
**IMPORTANT**: Do NOT iterate through individual IDs for large ranges!

Use range merging optimization:
1. Sort ranges by start position
2. Merge overlapping or adjacent ranges
3. Count total IDs: `sum(end - start + 1 for start, end in merged_ranges)`

This is O(n log n) instead of O(total_values), avoiding memory overflow.

## Notes

**Part 1:** Simple O(n*m) approach - check each available ID against all ranges  
**Part 2:** Range merging optimization required for large ranges

### Optimization Lesson
Initial naive approach used `set.update(range(start, end + 1))` which:
- ❌ Creates millions of individual integers in memory
- ❌ Causes memory overflow and extremely slow execution

Optimized approach uses range arithmetic:
- ✅ Works with range boundaries only
- ✅ O(n log n) time, O(n) space
- ✅ Handles ranges with billions of values efficiently
