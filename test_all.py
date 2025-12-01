"""
Quick test script to verify all days run without errors.
"""

import os
import sys
from pathlib import Path
import importlib.util


def test_day(day_num):
    """Test a specific day's solution."""
    day_dir = Path(__file__).parent / f"day{day_num:02d}"
    solution_file = day_dir / "solution.py"
    
    if not solution_file.exists():
        return None
    
    try:
        # Import the solution
        spec = importlib.util.spec_from_file_location(f"day{day_num:02d}", solution_file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[f"day{day_num:02d}"] = module
        
        # Suppress output during testing
        import io
        from contextlib import redirect_stdout, redirect_stderr
        
        f = io.StringIO()
        with redirect_stdout(f), redirect_stderr(f):
            spec.loader.exec_module(module)
            if hasattr(module, 'main'):
                module.main()
        
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main():
    """Test all available days."""
    print("Testing all solutions...\n")
    
    results = []
    for day_num in range(1, 26):
        day_dir = Path(__file__).parent / f"day{day_num:02d}"
        if day_dir.exists():
            print(f"Day {day_num:02d}...", end=" ")
            result = test_day(day_num)
            
            if result is None:
                print("⚠️  No solution found")
                results.append((day_num, "missing"))
            elif result:
                print("✅ Passed")
                results.append((day_num, "passed"))
            else:
                results.append((day_num, "failed"))
    
    print("\n" + "=" * 40)
    print("Summary:")
    print("=" * 40)
    
    passed = sum(1 for _, status in results if status == "passed")
    failed = sum(1 for _, status in results if status == "failed")
    missing = sum(1 for _, status in results if status == "missing")
    
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"⚠️  Missing: {missing}")
    
    if failed > 0:
        print("\nFailed days:")
        for day_num, status in results:
            if status == "failed":
                print(f"  - Day {day_num:02d}")


if __name__ == "__main__":
    main()
