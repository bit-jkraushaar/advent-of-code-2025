# Day 6: Trash Compactor

## Part 1

After jumping into a garbage chute, you find yourself in a garbage smasher with magnetically sealed doors. While waiting for cephalopods to open the door, you help with math homework.

The math worksheet consists of problems arranged horizontally. Each problem has:
- Numbers stacked vertically
- An operator (+, or *) at the bottom
- Problems separated by full columns of spaces

### Example:
```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

This represents four problems:
- `123 * 45 * 6 = 33210`
- `328 + 64 + 98 = 490`
- `51 * 387 * 215 = 4243455`
- `64 + 23 + 314 = 401`

Grand total: `33210 + 490 + 4243455 + 401 = 4277556`

**Task**: Calculate the grand total by solving all problems and adding the results.

## Part 2

The cephalopods explain that cephalopod math is written **right-to-left in columns**!

- Each column within a problem represents a digit position of the numbers
- Most significant digit is at the top, least significant at the bottom
- Numbers are read right-to-left within each problem

### Same example, different reading:
```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

Reading right-to-left, column by column:
- Rightmost problem: `4 + 431 + 623 = 1058`
- Second from right: `175 * 581 * 32 = 3253600`
- Third from right: `8 + 248 + 369 = 625`
- Leftmost problem: `356 * 24 * 1 = 8544`

Grand total: `1058 + 3253600 + 625 + 8544 = 3263827`

**Task**: Calculate the grand total using cephalopod math (right-to-left column reading).

## Notes

- Numbers can be multi-digit and may have different alignments within their problem
- Problems are separated by entirely empty columns
- The worksheet may be very wide and need to be "unrolled" completely
