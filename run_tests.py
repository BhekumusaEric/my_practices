#!/usr/bin/env python3
"""
Test runner script for Python Fundamentals Assessment Practice
Run this script to test your implementations
"""

import subprocess
import sys
import os

def run_tests():
    """Run all tests and display results"""
    print("=" * 60)
    print("PYTHON FUNDAMENTALS ASSESSMENT - TEST RUNNER")
    print("=" * 60)
    
    # Check if pytest is installed
    try:
        import pytest
    except ImportError:
        print("❌ pytest is not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
        print("✅ pytest installed successfully!")
    
    # Test files to run
    test_files = [
        "tests/test_list_operations.py",
        "tests/test_student_grades.py", 
        "tests/test_text_analyzer.py",
        "tests/test_sorting_algorithms.py",
        "tests/test_data_processor.py",
        "tests/test_math_utils.py"
    ]
    
    total_passed = 0
    total_failed = 0
    
    for test_file in test_files:
        if not os.path.exists(test_file):
            print(f"⚠️  Test file {test_file} not found, skipping...")
            continue
            
        print(f"\n🧪 Running {test_file}...")
        print("-" * 40)
        
        try:
            # Run pytest for this specific file
            result = subprocess.run([
                sys.executable, "-m", "pytest", test_file, "-v", "--tb=short"
            ], capture_output=True, text=True)
            
            print(result.stdout)
            if result.stderr:
                print("STDERR:", result.stderr)
            
            # Count passed/failed tests from output
            lines = result.stdout.split('\n')
            for line in lines:
                if ' failed' in line and ' passed' in line:
                    # Parse line like "2 failed, 3 passed in 0.05s"
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if part == 'passed':
                            total_passed += int(parts[i-1])
                        elif part == 'failed':
                            total_failed += int(parts[i-1])
                elif line.strip().endswith('passed') and 'failed' not in line:
                    # Parse line like "5 passed in 0.05s"
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if part == 'passed':
                            total_passed += int(parts[i-1])
                elif line.strip().endswith('failed') and 'passed' not in line:
                    # Parse line like "5 failed in 0.05s"
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if part == 'failed':
                            total_failed += int(parts[i-1])
            
        except Exception as e:
            print(f"❌ Error running {test_file}: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"✅ Total Passed: {total_passed}")
    print(f"❌ Total Failed: {total_failed}")
    print(f"📊 Success Rate: {total_passed/(total_passed+total_failed)*100:.1f}%" if (total_passed+total_failed) > 0 else "No tests run")
    
    if total_failed == 0 and total_passed > 0:
        print("\n🎉 Congratulations! All tests passed!")
        print("Remember to commit and push your code:")
        print("  git add .")
        print("  git commit -m 'Complete Python assessment'")
        print("  git push")
    elif total_failed > 0:
        print(f"\n⚠️  You have {total_failed} failing tests to fix.")
        print("Review the error messages above and fix your implementations.")
    else:
        print("\n❓ No tests were run. Make sure your function implementations are not just 'pass'.")

if __name__ == "__main__":
    run_tests()
