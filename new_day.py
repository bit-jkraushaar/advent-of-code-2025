"""
Create a new day directory with template files.

Usage: python new_day.py <day_number>
"""

import os
import sys
import shutil
from pathlib import Path


def create_new_day(day_num):
    """
    Create a new day directory with template files.
    
    Args:
        day_num: Day number (1-25)
    """
    if not 1 <= day_num <= 25:
        print("Error: Day number must be between 1 and 25.")
        return False
    
    base_dir = Path(__file__).parent
    day_dir = base_dir / f"day{day_num:02d}"
    
    if day_dir.exists():
        print(f"Error: Day {day_num} directory already exists.")
        return False
    
    # Create day directory
    day_dir.mkdir()
    print(f"Created directory: {day_dir}")
    
    # Copy template
    template_file = base_dir / "template.py"
    solution_file = day_dir / "solution.py"
    
    if template_file.exists():
        shutil.copy(template_file, solution_file)
        
        # Update day number in template
        with open(solution_file, 'r') as f:
            content = f.read()
        
        content = content.replace('Day XX', f'Day {day_num}')
        
        with open(solution_file, 'w') as f:
            f.write(content)
        
        print(f"Created solution file: {solution_file}")
    
    # Create empty input file
    input_file = day_dir / "input.txt"
    input_file.touch()
    print(f"Created input file: {input_file}")
    
    # Create README
    readme_file = day_dir / "README.md"
    readme_content = f"""# Day {day_num}: [Puzzle Title]

## Part 1

[Description of part 1]

## Part 2

[Description of part 2]

## Notes

[Any notes or observations about the puzzle]
"""
    
    with open(readme_file, 'w') as f:
        f.write(readme_content)
    
    print(f"Created README: {readme_file}")
    print(f"\nDay {day_num} setup complete!")
    print(f"\nNext steps:")
    print(f"1. Add your puzzle input to: {input_file}")
    print(f"2. Implement your solution in: {solution_file}")
    print(f"3. Run with: python run.py {day_num}")
    
    return True


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python new_day.py <day_number>")
        print("Example: python new_day.py 2")
        sys.exit(1)
    
    try:
        day_num = int(sys.argv[1])
        create_new_day(day_num)
    except ValueError:
        print("Error: Day number must be an integer.")
        sys.exit(1)


if __name__ == "__main__":
    main()
