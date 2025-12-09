"""Debug script for Day 8"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

example_data = [
    "162,817,812",
    "57,618,57",
    "906,360,560",
    "592,479,940",
    "352,342,300",
    "466,668,158",
    "542,29,236",
    "431,825,988",
    "739,650,466",
    "52,470,668",
    "216,146,977",
    "819,987,18",
    "117,168,530",
    "805,96,715",
    "346,949,466",
    "970,615,88",
    "941,993,340",
    "862,61,35",
    "984,92,344",
    "425,690,689",
]

# Parse coordinates
coords = []
for line in example_data:
    x, y, z = map(int, line.split(','))
    coords.append((x, y, z))

n = len(coords)
print(f"Number of junction boxes: {n}")

# Calculate all pairwise distances
distances = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, z1 = coords[i]
        x2, y2, z2 = coords[j]
        dist_sq = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
        dist = dist_sq ** 0.5
        distances.append((dist_sq, dist, i, j))

# Sort by distance
distances.sort()

print("\nFirst 20 closest pairs:")
for idx, (dist_sq, dist, i, j) in enumerate(distances[:20]):
    print(f"{idx+1}. Boxes {i} and {j}: distance = {dist:.2f}")

# Union-Find data structure
parent = list(range(n))
size = [1] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x == root_y:
        return False
    
    if size[root_x] < size[root_y]:
        parent[root_x] = root_y
        size[root_y] += size[root_x]
    else:
        parent[root_y] = root_x
        size[root_x] += size[root_y]
    
    return True

# Connect the 10 closest pairs
print("\nConnecting 10 closest pairs:")
connections = 0
for dist_sq, dist, i, j in distances:
    if connections >= 10:
        break
    if union(i, j):
        connections += 1
        print(f"  Connection {connections}: boxes {i} and {j} (distance {dist:.2f})")
    else:
        print(f"  Skipped: boxes {i} and {j} already connected (distance {dist:.2f})")

# Find all circuit sizes
circuit_sizes = {}
for i in range(n):
    root = find(i)
    circuit_sizes[root] = size[root]

sizes = sorted(circuit_sizes.values(), reverse=True)
print(f"\nCircuit sizes: {sizes}")
print(f"Number of circuits: {len(sizes)}")
print(f"Three largest: {sizes[0]}, {sizes[1]}, {sizes[2]}")
print(f"Product: {sizes[0] * sizes[1] * sizes[2]}")
