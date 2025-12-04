# Day 4: Printing Department

## Part 1

The printing department has rolls of paper (@) arranged on a grid. Forklifts can only access a roll if there are **fewer than 4 rolls** in the 8 adjacent positions (including diagonals).

**Task:** Count how many rolls of paper can be accessed by a forklift.

### Example
```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

In this example, 13 rolls can be accessed (those with fewer than 4 adjacent rolls).

## Part 2

Once accessible rolls are removed, more rolls may become accessible. The task is to keep removing accessible rolls iteratively until no more can be removed.

**Task:** Count the total number of rolls that can be removed through this iterative process.

### Example Process
Starting with the same grid, the removal happens in waves:
- Wave 1: Remove 13 rolls (initially accessible)
- Wave 2: Remove 12 rolls (newly accessible after wave 1)
- Wave 3: Remove 7 rolls
- Wave 4: Remove 5 rolls
- Wave 5: Remove 2 rolls
- Waves 6-9: Remove 1 roll each

**Total:** 43 rolls removed

## Notes

**Solution Approach:**
1. Parse the grid into a 2D structure
2. For each position containing a roll (@):
   - Count adjacent rolls in all 8 directions
   - If count < 4, increment accessible counter
3. Return the total count

**Key Points:**
- Adjacent means all 8 surrounding cells (including diagonals)
- Empty cells (.) don't count
- Boundary cells have fewer potential neighbors

