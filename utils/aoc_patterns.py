"""
Common Python patterns and snippets for Advent of Code solutions.
Reference this file when implementing new days.
"""

# ============================================================================
# INPUT PARSING
# ============================================================================

# Lines of text
lines = read_input('input.txt')  # ['line1', 'line2', ...]

# List of integers
numbers = [int(x) for x in read_input('input.txt')]

# Comma-separated numbers
numbers = [int(x) for x in read_input('input.txt')[0].split(',')]

# Grid/2D array as list of lists
grid = [list(line) for line in read_input('input.txt')]

# Grid as dictionary {(x, y): value}
grid = {(x, y): char 
        for y, line in enumerate(read_input('input.txt'))
        for x, char in enumerate(line)}

# Groups separated by blank lines
groups = read_input_groups('input.txt')  # [['group1line1', ...], ['group2line1', ...]]

# Parse structured lines (e.g., "move 5 from 2 to 1")
import re
for line in read_input('input.txt'):
    nums = list(map(int, re.findall(r'-?\d+', line)))
    # or
    match = re.match(r'(\w+) (\d+)', line)
    command, value = match.groups()


# ============================================================================
# DATA STRUCTURES
# ============================================================================

from collections import defaultdict, deque, Counter

# Graph as adjacency list
graph = defaultdict(list)
graph[node].append(neighbor)

# Frequency counting
counts = Counter(items)
most_common = counts.most_common(5)

# BFS queue
queue = deque([start_state])

# Priority queue (Dijkstra, A*)
import heapq
heap = []
heapq.heappush(heap, (priority, item))
priority, item = heapq.heappop(heap)

# Set operations
visited = set()
visited.add((x, y))
if (x, y) not in visited:
    # ...


# ============================================================================
# GRID/MAP NAVIGATION
# ============================================================================

# 4-directional movement (up, down, left, right)
DIRS_4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# or
DIRS_4 = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

# 8-directional movement (including diagonals)
DIRS_8 = [(0, 1), (0, -1), (1, 0), (-1, 0), 
          (1, 1), (1, -1), (-1, 1), (-1, -1)]

# Get neighbors
def get_neighbors(x, y, grid):
    neighbors = []
    for dx, dy in DIRS_4:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors

# Grid bounds check
def in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


# ============================================================================
# SEARCH ALGORITHMS
# ============================================================================

# BFS (shortest path in unweighted graph)
def bfs(start, goal, get_neighbors_func):
    queue = deque([(start, 0)])  # (state, distance)
    visited = {start}
    
    while queue:
        state, dist = queue.popleft()
        
        if state == goal:
            return dist
        
        for neighbor in get_neighbors_func(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    
    return -1  # Not found


# DFS (depth-first search)
def dfs(node, visited, graph):
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)


# Dijkstra (shortest path with weights)
def dijkstra(start, goal, get_neighbors_func):
    heap = [(0, start)]  # (cost, state)
    costs = {start: 0}
    
    while heap:
        cost, state = heapq.heappop(heap)
        
        if state == goal:
            return cost
        
        if cost > costs.get(state, float('inf')):
            continue
        
        for neighbor, edge_cost in get_neighbors_func(state):
            new_cost = cost + edge_cost
            if new_cost < costs.get(neighbor, float('inf')):
                costs[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    
    return -1  # Not found


# ============================================================================
# COMMON PATTERNS
# ============================================================================

# Simulate steps until condition
def simulate(state, steps):
    for step in range(steps):
        state = update(state)
        if check_condition(state):
            return step
    return state


# Find cycle (for infinite loops)
def find_cycle(start_state, step_func):
    seen = {start_state: 0}
    state = start_state
    step = 0
    
    while True:
        state = step_func(state)
        step += 1
        
        if state in seen:
            cycle_start = seen[state]
            cycle_length = step - cycle_start
            return cycle_start, cycle_length
        
        seen[state] = step


# Manhattan distance
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Range overlap
def ranges_overlap(r1, r2):
    return r1[0] <= r2[1] and r2[0] <= r1[1]


# Merge overlapping ranges
def merge_ranges(ranges):
    if not ranges:
        return []
    
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    
    for start, end in sorted_ranges[1:]:
        if start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    return merged


# ============================================================================
# MATH UTILITIES
# ============================================================================

import math

# GCD and LCM
gcd = math.gcd(a, b)
lcm = a * b // math.gcd(a, b)

# LCM of multiple numbers
from functools import reduce
lcm_all = reduce(lambda a, b: a * b // math.gcd(a, b), numbers)

# Modular arithmetic
result = (a + b) % mod
result = (a * b) % mod
result = pow(a, b, mod)  # (a^b) % mod


# ============================================================================
# STRING OPERATIONS
# ============================================================================

# Split and parse
parts = line.split()
nums = list(map(int, line.split()))

# Replace multiple characters
text = text.translate(str.maketrans('abc', 'xyz'))

# Check if string contains only certain characters
if all(c in '01' for c in text):
    # binary string


# ============================================================================
# ITERATION HELPERS
# ============================================================================

from itertools import combinations, permutations, product, cycle, islice

# All pairs
for a, b in combinations(items, 2):
    # ...

# All permutations
for perm in permutations(items):
    # ...

# Cartesian product
for a, b, c in product(range(10), range(10), range(10)):
    # ...

# Sliding window
def sliding_window(seq, n):
    it = iter(seq)
    window = list(islice(it, n))
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window = window[1:] + [item]
        yield tuple(window)


# Pairwise (Python 3.10+)
from itertools import pairwise
for a, b in pairwise([1, 2, 3, 4]):
    # (1,2), (2,3), (3,4)
    pass


# ============================================================================
# DEBUGGING
# ============================================================================

# Print grid
def print_grid(grid):
    for row in grid:
        print(''.join(str(c) for c in row))

# Print dict grid
def print_dict_grid(grid):
    min_x = min(x for x, y in grid)
    max_x = max(x for x, y in grid)
    min_y = min(y for x, y in grid)
    max_y = max(y for x, y in grid)
    
    for y in range(min_y, max_y + 1):
        print(''.join(grid.get((x, y), ' ') for x in range(min_x, max_x + 1)))


# ============================================================================
# MEMOIZATION
# ============================================================================

from functools import lru_cache

@lru_cache(maxsize=None)
def expensive_function(n):
    # Recursive or expensive computation
    if n <= 1:
        return 1
    return expensive_function(n - 1) + expensive_function(n - 2)


# ============================================================================
# BINARY/BIT OPERATIONS
# ============================================================================

# Check if bit is set
if num & (1 << i):
    # bit i is set

# Set bit
num |= (1 << i)

# Clear bit
num &= ~(1 << i)

# Toggle bit
num ^= (1 << i)

# Count set bits
bin(num).count('1')


# ============================================================================
# COORDINATE TRANSFORMS
# ============================================================================

# Rotate 90 degrees clockwise
def rotate_cw(x, y):
    return y, -x

# Rotate 90 degrees counter-clockwise
def rotate_ccw(x, y):
    return -y, x

# Rotate 180 degrees
def rotate_180(x, y):
    return -x, -y

# Reflect over x-axis
def reflect_x(x, y):
    return x, -y

# Reflect over y-axis
def reflect_y(x, y):
    return -x, y
