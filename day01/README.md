# Day 1: Secret Entrance

## Part 1

The safe has a circular dial (0-99) that starts at position 50. Follow rotation instructions (L for left/lower, R for right/higher) and count how many times the dial ends on 0 after a rotation.

**Example:**
```
L68, L30, R48, L5, R60, L55, L1, L99, R14, L82
```
Result: **3** (dial ends on 0 three times)

## Part 2

Method 0x434C49434B: Count **every** time the dial passes through 0 during any click, not just when it ends on 0.

**Example:**
```
L68, L30, R48, L5, R60, L55, L1, L99, R14, L82
```
Result: **6** (3 times at end of rotation + 3 times during rotations)

## Algorithm

### Part 1
- Simulate each rotation using modular arithmetic: `(position ± distance) % 100`
- Count when final position equals 0

### Part 2
- Simulate each individual click
- Count every time position equals 0 during the rotation
- Note: A large rotation like R1000 from position 50 crosses 0 multiple times

## Solutions

- Part 1: **982**
- Part 2: **6106**
