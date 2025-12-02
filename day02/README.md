# Day 2: Gift Shop

## Part 1

Find invalid product IDs in the gift shop database. An invalid ID is made only of some sequence of digits repeated exactly twice.

Examples:
- `55` (5 repeated twice)
- `6464` (64 repeated twice)
- `123123` (123 repeated twice)

**Answer:** 12850231731

## Part 2

Now an ID is invalid if it's made only of some sequence of digits repeated **at least** twice.

Examples:
- `12341234` (1234 two times)
- `123123123` (123 three times)
- `1212121212` (12 five times)
- `1111111` (1 seven times)

**Answer:** 24774350322

## Notes

- Part 1 requires checking if a number can be split exactly in half with both halves being identical
- Part 2 requires checking all possible pattern lengths that could divide evenly into the number
- The key insight is that for Part 2, we need to check if the number's string representation can be formed by repeating a pattern at least twice
- Pattern lengths range from 1 (single digit repeated) to length/2 (half the number repeated twice)
