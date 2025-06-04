#!/usr/bin/env python3
"""
Quick Start Guide for Python Assessment Practice
"""

def show_progress():
    """Show current progress on all problems"""
    import subprocess
    import sys
    
    print("🎯 PYTHON ASSESSMENT PRACTICE - PROGRESS CHECK")
    print("=" * 60)
    
    # Check each problem file
    problems = [
        ("List Operations", "list_operations.py", "tests/test_list_operations.py"),
        ("Student Grades", "student_grades.py", "tests/test_student_grades.py"),
        ("Text Analyzer", "text_analyzer.py", "tests/test_text_analyzer.py"),
        ("Sorting Algorithms", "sorting_algorithms.py", "tests/test_sorting_algorithms.py"),
        ("Data Processor", "data_processor.py", "tests/test_data_processor.py"),
        ("Math Utils", "math_utils.py", "tests/test_math_utils.py")
    ]
    
    total_passed = 0
    total_failed = 0
    
    for name, file, test_file in problems:
        print(f"\n📝 {name}")
        print("-" * 30)
        
        try:
            result = subprocess.run([
                sys.executable, "-m", "pytest", test_file, "-v", "--tb=no", "-q"
            ], capture_output=True, text=True)
            
            # Count results
            output = result.stdout
            if "passed" in output:
                lines = output.split('\n')
                for line in lines:
                    if 'passed' in line and 'failed' in line:
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if part == 'passed':
                                passed = int(parts[i-1])
                                total_passed += passed
                            elif part == 'failed':
                                failed = int(parts[i-1])
                                total_failed += failed
                        print(f"   ✅ {passed} passed, ❌ {failed} failed")
                        break
                    elif line.strip().endswith('passed'):
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if part == 'passed':
                                passed = int(parts[i-1])
                                total_passed += passed
                        print(f"   ✅ {passed} passed, ❌ 0 failed")
                        break
                else:
                    print("   ❓ No tests run (functions not implemented)")
            else:
                print("   ❓ No tests run (functions not implemented)")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print(f"\n{'='*60}")
    print(f"📊 OVERALL PROGRESS")
    print(f"{'='*60}")
    print(f"✅ Total Passed: {total_passed}")
    print(f"❌ Total Failed: {total_failed}")
    
    if total_passed + total_failed > 0:
        success_rate = total_passed / (total_passed + total_failed) * 100
        print(f"📈 Success Rate: {success_rate:.1f}%")
    else:
        print("📈 Success Rate: 0% (No functions implemented yet)")
    
    print(f"\n💡 NEXT STEPS:")
    if total_failed > 0:
        print(f"   1. Pick a problem file to work on")
        print(f"   2. Read the function docstrings and examples")
        print(f"   3. Look at the test cases to understand requirements")
        print(f"   4. Implement the function")
        print(f"   5. Run tests: python3 -m pytest tests/test_[filename].py -v")
        print(f"   6. Commit when working: git add . && git commit -m 'message'")
    else:
        print(f"   🎉 All done! Remember to push your code!")

if __name__ == "__main__":
    show_progress()
