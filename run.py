"""
Advent of Code 2025 - Main Runner

Run solutions for specific days or all days.
"""

import os
import sys
import importlib.util
from pathlib import Path


def get_day_directories():
    """Get all day directories in sorted order."""
    base_dir = Path(__file__).parent
    day_dirs = []
    
    for item in base_dir.iterdir():
        if item.is_dir() and item.name.startswith('day') and item.name[3:].isdigit():
            day_dirs.append(item)
    
    return sorted(day_dirs, key=lambda x: int(x.name[3:]))


def run_day(day_num):
    """
    Run the solution for a specific day.
    
    Args:
        day_num: Day number (1-25)
    """
    day_dir = Path(__file__).parent / f"day{day_num:02d}"
    solution_file = day_dir / "solution.py"
    
    if not solution_file.exists():
        print(f"Day {day_num} solution not found.")
        return False
    
    # Import and run the solution
    spec = importlib.util.spec_from_file_location(f"day{day_num:02d}", solution_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"day{day_num:02d}"] = module
    spec.loader.exec_module(module)
    
    if hasattr(module, 'main'):
        module.main()
        return True
    else:
        print(f"No main() function found in day {day_num} solution.")
        return False


def run_all_days():
    """Run solutions for all available days."""
    day_dirs = get_day_directories()
    
    if not day_dirs:
        print("No day solutions found.")
        return
    
    for day_dir in day_dirs:
        day_num = int(day_dir.name[3:])
        print(f"\n{'=' * 60}")
        run_day(day_num)
        print('=' * 60)


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        try:
            day_num = int(sys.argv[1])
            if 1 <= day_num <= 25:
                run_day(day_num)
            else:
                print("Day number must be between 1 and 25.")
        except ValueError:
            if sys.argv[1].lower() == 'all':
                run_all_days()
            else:
                print("Invalid argument. Use a day number (1-25) or 'all'.")
    else:
        # No arguments - run all days
        run_all_days()


if __name__ == "__main__":
    main()
