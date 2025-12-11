"""
Advent of Code 2025 - Day 11: Reactor

Find all paths from 'you' to 'out' through a graph of connected devices.
Uses dynamic programming to count paths efficiently.
"""

import os
import sys
from collections import defaultdict, deque

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_reader import read_input


def solve_part1(data):
    """
    Part 1: Count all paths from 'you' to 'out'
    
    Uses DP to count paths instead of enumerating them (avoids exponential explosion).
    
    Args:
        data: Puzzle input data (list of lines describing device connections)
    
    Returns:
        Number of different paths from 'you' to 'out'
    """
    # Build the graph of connections
    graph = defaultdict(list)
    
    for line in data:
        parts = line.split(': ')
        device = parts[0]
        outputs = parts[1].split()
        graph[device] = outputs
    
    # Use BFS with path counting (dynamic programming approach)
    # Instead of tracking individual paths, track how many paths reach each node
    path_count = defaultdict(int)
    path_count['you'] = 1
    
    # BFS to process nodes in order
    queue = deque(['you'])
    visited = set()
    processing_order = []
    
    # First, get topological order of nodes
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        processing_order.append(current)
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)
    
    # Now process in order, accumulating path counts
    for node in processing_order:
        if node == 'you':
            continue
        # Count paths to this node from all predecessors
        count = 0
        for predecessor in graph:
            if node in graph[predecessor]:
                count += path_count[predecessor]
        path_count[node] = count
    
    return path_count.get('out', 0)


def solve_part2(data):
    """
    Part 2: Count paths from 'svr' to 'out' that visit both 'dac' and 'fft'
    
    Key insight: Instead of tracking visited nodes in the state, we use a different approach:
    Count paths in 3 phases: svr->dac, dac->fft (or fft->dac), then to out.
    This exploits the structure that both dac and fft must be visited.
    
    Args:
        data: Puzzle input data (list of lines describing device connections)
    
    Returns:
        Number of paths from 'svr' to 'out' that visit both 'dac' and 'fft'
    """
    # Build the graph of connections
    graph = defaultdict(list)
    
    for line in data:
        parts = line.split(': ')
        device = parts[0]
        outputs = parts[1].split()
        graph[device] = outputs
    
    # Memoized DFS without visited set in memo key
    # Key insight: if graph is a DAG, we don't need visited in state
    memo = {}
    
    def count_paths_simple(start, end, visited):
        if start == end:
            return 1
        if start in visited:
            return 0
        
        # Try without visited in memo for DAG-like structure
        if start in memo and end in memo[start]:
            return memo[start][end]
        
        new_visited = visited | {start}
        total = 0
        for neighbor in graph.get(start, []):
            total += count_paths_simple(neighbor, end, new_visited)
        
        if start not in memo:
            memo[start] = {}
        memo[start][end] = total
        return total
    
    # Count paths that go: svr -> ... -> dac -> ... -> fft -> ... -> out
    paths_svr_dac_fft = 0
    if 'dac' in graph and 'fft' in graph:
        for path_to_dac in range(1):  # We need to enumerate differently
            pass
    
    # Actually, let's use the DP approach properly:
    # State is (current_node, visited_dac, visited_fft)
    # But don't include full visited set
    memo2 = {}
    
    def dp_count(node, has_dac, has_fft):
        if node == 'out':
            return 1 if (has_dac and has_fft) else 0
        
        state = (node, has_dac, has_fft)
        if state in memo2:
            return memo2[state]
        
        new_dac = has_dac or (node == 'dac')
        new_fft = has_fft or (node == 'fft')
        
        total = 0
        for neighbor in graph.get(node, []):
            total += dp_count(neighbor, new_dac, new_fft)
        
        memo2[state] = total
        return total
    
    return dp_count('svr', False, False)


def main():
    """Main entry point for Day 11 solution."""
    # Example test data from puzzle description - Part 1
    example_data_part1 = [
        "aaa: you hhh",
        "you: bbb ccc",
        "bbb: ddd eee",
        "ccc: ddd eee fff",
        "ddd: ggg",
        "eee: out",
        "fff: out",
        "ggg: out",
        "hhh: ccc fff iii",
        "iii: out"
    ]
    
    # Example test data from puzzle description - Part 2
    example_data_part2 = [
        "svr: aaa bbb",
        "aaa: fft",
        "fft: ccc",
        "bbb: tty",
        "tty: ccc",
        "ccc: ddd eee",
        "ddd: hub",
        "hub: fff",
        "eee: dac",
        "dac: fff",
        "fff: ggg hhh",
        "ggg: out",
        "hhh: out"
    ]
    
    # Test with example
    print("=== Day 11: Reactor ===\n")
    
    print("Testing with Part 1 example:")
    example_part1 = solve_part1(example_data_part1)
    print(f"  Part 1: {example_part1} (expected: 5)")
    
    print("\nTesting with Part 2 example:")
    example_part2 = solve_part2(example_data_part2)
    print(f"  Part 2: {example_part2} (expected: 2)")
    print()
    
    # Solve actual puzzle
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    
    try:
        data = read_input(input_file)
        
        part1_answer = solve_part1(data)
        part2_answer = solve_part2(data)
        
        print("Puzzle answers:")
        print(f"  Part 1: {part1_answer}")
        print(f"  Part 2: {part2_answer}")
        
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        print("Please add your puzzle input to solve the actual puzzle.")


if __name__ == "__main__":
    main()
