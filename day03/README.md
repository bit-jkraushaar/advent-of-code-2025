# Day 3: Lobby

## Part 1

You need to power an escalator using batteries. Each line represents a bank of batteries with joltage ratings (digits 1-9). You must turn on exactly 2 batteries per bank to produce a joltage equal to the 2-digit number formed by those two digits. Find the maximum joltage possible from each bank and sum them.

For each bank:
- Select exactly 2 batteries in their original order (positions i and j where i < j)
- The joltage produced is the 2-digit number formed by those batteries
- Find the maximum possible joltage for each bank
- Return the sum of all maximum joltages

Example:
- `987654321111111` → max is 98 (first two batteries)
- `811111111111119` → max is 89 (batteries at positions 0 and 14)
- `234234234234278` → max is 78 (last two batteries)
- `818181911112111` → max is 92 (positions 0 and 6)
- Total: 98 + 89 + 78 + 92 = 357

## Part 2

Now you need to select exactly 12 batteries from each bank to maximize the joltage (forming a 12-digit number).

For each bank:
- Select exactly 12 batteries in their original order
- The joltage produced is the 12-digit number formed by those batteries
- Find the maximum possible joltage for each bank
- Return the sum of all maximum joltages

Example:
- `987654321111111` → max is 987654321111 (remove three 1s at the end)
- `811111111111119` → max is 811111111119 (remove three 1s)
- `234234234234278` → max is 434234234278 (remove 2, 3, 2 near start)
- `818181911112111` → max is 888911112111 (remove some 1s near front)
- Total: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619

## Notes

- Batteries cannot be rearranged - we must maintain their original order
- Each bank can have a different number of batteries

**Part 1 Solution**: Brute force - try all pairs of positions (i, j) where i < j
- Time Complexity: O(n * m²) where n is the number of banks and m is the length of each bank

**Part 2 Solution**: Greedy algorithm to remove digits that minimize the result
- To maximize a number when selecting k digits, we remove (n-k) digits
- Greedy approach: repeatedly remove the first digit that is smaller than its successor
- If no such digit exists (descending sequence), remove the last digit
- This is equivalent to the classic "Remove K Digits" problem
- Time Complexity: O(n * m * r) where r is the number of digits to remove
