"""
Advent of Code 2025 - Day 8: Playground

Connect junction boxes using minimum spanning tree approach.
Find the 1000 shortest connections and multiply the sizes of the 3 largest circuits.
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def solve_part1(data, num_connections=1000):
    """
    Part 1: Connect closest junction box pairs and find product of 3 largest circuits.
    
    Uses Union-Find to track circuits as we connect junction boxes.
    
    Args:
        data: List of coordinate strings in format "x,y,z"
        num_connections: Number of connections to make (default 1000)
    
    Returns:
        Product of the three largest circuit sizes
    """
    # Parse coordinates
    coords = []
    for line in data:
        x, y, z = map(int, line.split(','))
        coords.append((x, y, z))
    
    n = len(coords)
    
    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = coords[i]
            x2, y2, z2 = coords[j]
            dist_sq = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
            distances.append((dist_sq, i, j))
    
    # Sort by distance
    distances.sort()
    
    # Union-Find data structure
    parent = list(range(n))
    size = [1] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        
        if root_x == root_y:
            return False  # Already connected
        
        # Union by size
        if size[root_x] < size[root_y]:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
        else:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
        
        return True
    
    # Attempt to connect the first num_connections closest pairs
    # (some may already be connected)
    for idx in range(min(num_connections, len(distances))):
        dist_sq, i, j = distances[idx]
        union(i, j)  # Try to connect (returns False if already connected)
    
    # Find all circuit sizes
    circuit_sizes = {}
    for i in range(n):
        root = find(i)
        circuit_sizes[root] = size[root]
    
    # Get the three largest circuit sizes
    sizes = sorted(circuit_sizes.values(), reverse=True)
    
    # Multiply the three largest (handle case with fewer than 3 circuits)
    if len(sizes) >= 3:
        return sizes[0] * sizes[1] * sizes[2]
    elif len(sizes) == 2:
        return sizes[0] * sizes[1]
    elif len(sizes) == 1:
        return sizes[0]
    else:
        return 0


def solve_part2(data):
    """
    Part 2: Find the connection that completes the circuit.
    
    Continue connecting closest pairs until all junction boxes are in one circuit.
    Return the product of the X coordinates of the last two boxes connected.
    
    Args:
        data: List of coordinate strings in format "x,y,z"
    
    Returns:
        Product of X coordinates of the final connecting pair
    """
    # Parse coordinates
    coords = []
    for line in data:
        x, y, z = map(int, line.split(','))
        coords.append((x, y, z))
    
    n = len(coords)
    
    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = coords[i]
            x2, y2, z2 = coords[j]
            dist_sq = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
            distances.append((dist_sq, i, j))
    
    # Sort by distance
    distances.sort()
    
    # Union-Find data structure
    parent = list(range(n))
    size = [1] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        
        if root_x == root_y:
            return False  # Already connected
        
        # Union by size
        if size[root_x] < size[root_y]:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
        else:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
        
        return True
    
    def num_circuits():
        """Count the number of distinct circuits."""
        return len(set(find(i) for i in range(n)))
    
    # Connect pairs until we have just one circuit
    for dist_sq, i, j in distances:
        if union(i, j):
            # Check if this connection completed the circuit
            if num_circuits() == 1:
                # This was the final connection!
                x1, y1, z1 = coords[i]
                x2, y2, z2 = coords[j]
                return x1 * x2
    
    return 0  # Should not reach here if input is valid


def main():
    """Main entry point for Day 8 solution."""
    # Example test data
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
    
    # Test with example
    print("=== Day 8: Playground ===\n")
    
    print("Testing with example (10 connections):")
    example_part1 = solve_part1(example_data, num_connections=10)
    print(f"  Part 1: {example_part1} (expected: 40)")
    
    example_part2 = solve_part2(example_data)
    print(f"  Part 2: {example_part2} (expected: 25272)")
    print()
    
    # Solve actual puzzle
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    
    try:
        data = read_input(input_file)
        
        part1_answer = solve_part1(data)
        print("Puzzle answers:")
        print(f"  Part 1: {part1_answer}")
        
        part2_answer = solve_part2(data)
        print(f"  Part 2: {part2_answer}")
        
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        print("Please add your puzzle input to solve the actual puzzle.")


if __name__ == "__main__":
    main()
