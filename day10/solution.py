"""
Advent of Code 2025 - Day 10: Factory

Part 1: Toggle lights (GF(2))
Part 2: Linear system solver
"""

import os
import sys
import re
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.input_reader import read_input


def parse_machine(line):
    """Parse machine configuration."""
    lights_match = re.search(r'\[([.#]+)\]', line)
    target = [1 if c == '#' else 0 for c in lights_match.group(1)]
    
    buttons = []
    for match in re.finditer(r'\(([0-9,]+)\)', line):
        buttons.append([int(x) for x in match.group(1).split(',')])
    
    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    joltage = [int(x) for x in joltage_match.group(1).split(',')]
    
    return target, buttons, joltage


def solve_part1_machine(target, buttons):
    """Solve Part 1 - toggle lights."""
    for size in range(len(buttons) + 1):
        for combo in combinations(range(len(buttons)), size):
            state = [0] * len(target)
            for button_idx in combo:
                for light_idx in buttons[button_idx]:
                    state[light_idx] ^= 1
            if state == target:
                return size
    return 0


def solve_part2_machine(joltage, buttons):
    """Solve Part 2 - ILP to find minimum button presses."""
    import pulp
    
    n_buttons = len(buttons)
    n_counters = len(joltage)
    
    # Create sparse constraint matrix
    constraints = [[] for _ in range(n_counters)]
    for btn_idx, button in enumerate(buttons):
        for counter_idx in button:
            constraints[counter_idx].append(btn_idx)
    
    # Create the ILP problem
    prob = pulp.LpProblem("J", pulp.LpMinimize)
    
    # Variables: how many times to press each button
    b = [pulp.LpVariable(f"b{i}", 0, None, 'Integer') for i in range(n_buttons)]
    
    # Objective: minimize total button presses
    prob += pulp.lpSum(b)
    
    # Constraints: each counter must reach exactly its target joltage
    for i in range(n_counters):
        if constraints[i]:
            prob += pulp.lpSum(b[j] for j in constraints[i]) == joltage[i]
    
    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    
    return int(pulp.value(prob.objective)) if prob.status == pulp.LpStatusOptimal else 0


def solve_part1(data):
    """Part 1: Toggle lights."""
    total = 0
    for line in data:
        target, buttons, _ = parse_machine(line)
        total += solve_part1_machine(target, buttons)
    return total


def solve_part2(data):
    """Part 2: Joltage configuration."""
    total = 0
    for line in data:
        _, buttons, joltage = parse_machine(line)
        total += solve_part2_machine(joltage, buttons)
    return total


def main():
    """Main entry point."""
    example_data = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    ]
    
    print("=== Day 10: Factory ===\n")
    print("Testing with example:")
    print(f"  Part 1: {solve_part1(example_data)} (expected: 7)")
    print(f"  Part 2: {solve_part2(example_data)} (expected: 33)")
    print()
    
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    try:
        data = read_input(input_file)
        print("Puzzle answers:")
        print(f"  Part 1: {solve_part1(data)}")
        print(f"  Part 2: {solve_part2(data)}")
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")


if __name__ == "__main__":
    main()
