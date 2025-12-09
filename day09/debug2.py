example_data = [
    "7,1",
    "11,1",
    "11,7",
    "9,7",
    "9,5",
    "2,5",
    "2,3",
    "7,3"
]

red_tiles = []
for line in example_data:
    x, y = map(int, line.split(','))
    red_tiles.append((x, y))

red_green = set(red_tiles)

for i in range(len(red_tiles)):
    x1, y1 = red_tiles[i]
    x2, y2 = red_tiles[(i + 1) % len(red_tiles)]
    
    if x1 == x2:  # Vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            red_green.add((x1, y))
    else:  # Horizontal
        for x in range(min(x1, x2), max(x1, x2) + 1):
            red_green.add((x, y1))

print(f"Boundary tiles: {len(red_green)}")
print(f"Red+Green boundary: {sorted(red_green)[:20]}")

# Show what tiles we have at y=3
y3_tiles = sorted([x for x, y in red_green if y == 3])
print(f"Tiles at y=3: {y3_tiles}")

# Check rect from (2,3) to (9,5)
print(f"\nChecking rectangle (2,3) to (9,5):")
print(f"Should have area 24: {(9-2+1) * (5-3+1)}")
for y in range(3, 6):
    row_tiles = sorted([x for x, y2 in red_green if y2 == y])
    print(f"  y={y}: {row_tiles}")
