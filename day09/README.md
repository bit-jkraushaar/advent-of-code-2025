# Day 9: Movie Theater

## Part 1

Find the largest rectangle that can be formed using red tiles as opposite corners in a grid.

**Approach:**
- Parse red tile coordinates from input (format: "x,y")
- For each pair of red tiles that differ in both x and y coordinates (can form opposite corners)
- Calculate rectangle area: (|x2-x1| + 1) * (|y2-y1| + 1)
- Track maximum area found

**Notes:**
- The area includes both corner tiles, so we add 1 to each dimension
- Time complexity: O(n²) where n is the number of red tiles
- Straightforward brute force works fine for Part 1

## Part 2

Find the largest rectangle with red corners that only contains red or green tiles.

**Problem:**
- Green tiles connect consecutive red tiles in the input list (wrapping around)
- Green tiles also fill the interior of the polygon formed by red tiles
- Rectangle must have red tiles at opposite corners
- All other tiles in the rectangle must be red or green (no "other" tiles)

**Initial Failed Approaches:**
1. **Precompute all green tiles** - Too slow with huge coordinate range (89k-98k)
2. **On-demand point-in-polygon checks** - Still too slow checking millions of points
3. **Interval-based validation** - Complex and still slow with large coordinate space
4. **Memoized validation** - Better but still too slow for 50k+ rows

**Final Solution: Coordinate Compression**
- Map actual coordinates (89k-98k range) to compressed indices (0-496 range)
- Build a compact 496×496 boolean grid instead of 10k×50k grid
- Fill the grid:
  1. Mark red tiles
  2. Add green connecting lines between consecutive red tiles
  3. Use scanline algorithm to fill polygon interior
- For each red tile pair, check compressed rectangle in O(area) time
- Calculate area using original coordinates

**Key Insight:**
With 496 red tiles, there are only 496 unique x-coordinates and 496 unique y-coordinates that matter. Everything else is wasted space. By compressing coordinates, the grid becomes manageable.

**Credit:**
Solution inspired by Reddit community hint about coordinate compression:
https://www.reddit.com/r/adventofcode/comments/1pi0pek/2025_day_9_part_2/

## Lessons Learned

1. **Sparse vs Dense Grids:** When coordinates are sparse (few used coordinates in a huge range), coordinate compression is essential

2. **Algorithm Selection:** Sometimes the "obvious" algorithm (fill all points, check all rectangles) doesn't scale. Need to think about the actual data structure:
   - Bad: 10,000 × 50,000 grid = 500M points
   - Good: 496 × 496 compressed grid = 246K points (2000x smaller!)

3. **Don't Assume AI Knows Best:** This problem stumped the AI initially. Multiple approaches failed before finding the right one. Sometimes human insights (like the Reddit hint about coordinate compression) are crucial.

4. **Profile Before Optimizing:** The bottleneck wasn't the algorithm logic, it was iterating over millions of unused coordinates. Identifying the real problem (coordinate space) led to the solution.

5. **Check Input Characteristics:** Looking at the actual input revealed:
   - Only 496 red tiles
   - Coordinates range from 89k-98k (huge, sparse space)
   - Only 496 unique x-values and 496 unique y-values used
   - This analysis directly led to the coordinate compression solution

## Notes

[Any notes or observations about the puzzle]
