#!/usr/bin/env python3
"""
API Learning Progress Checker 📊

Check your progress through the API learning curriculum.
"""

import subprocess
import sys
import os
import importlib.util


def check_lesson_completion():
    """
    Check which lessons have been completed
    """
    print("📚 Lesson Completion Status:")
    print("-" * 40)
    
    lessons = [
        ("lesson_01_what_are_apis.py", "What Are APIs?"),
        ("lesson_02_http_basics.py", "HTTP Basics"),
        ("lesson_03_first_api_call.py", "First API Call"),
    ]
    
    completed_lessons = 0
    
    for lesson_file, lesson_name in lessons:
        lesson_path = f"lessons/{lesson_file}"
        if os.path.exists(lesson_path):
            print(f"  ✅ {lesson_name}")
            completed_lessons += 1
        else:
            print(f"  ❌ {lesson_name} (file missing)")
    
    print(f"\nLessons available: {completed_lessons}/{len(lessons)}")
    return completed_lessons


def check_problem_solutions():
    """
    Check which problems have been attempted
    """
    print("\n🧪 Problem Solution Status:")
    print("-" * 40)
    
    problems = [
        ("problem_01_api_concepts.py", "API Concepts"),
        ("problem_02_http_concepts.py", "HTTP Concepts"),
        ("problem_03_first_requests.py", "First Requests"),
    ]
    
    attempted_problems = 0
    
    for problem_file, problem_name in problems:
        problem_path = f"problems/{problem_file}"
        if os.path.exists(problem_path):
            # Check if functions have been implemented (not just 'pass')
            try:
                with open(problem_path, 'r') as f:
                    content = f.read()
                    
                # Count functions that still have 'pass'
                pass_count = content.count('pass')
                total_functions = content.count('def ') - 1  # Exclude main/test functions
                
                if pass_count < total_functions:
                    print(f"  🔄 {problem_name} (partially completed)")
                    attempted_problems += 0.5
                elif pass_count == 0:
                    print(f"  ✅ {problem_name} (completed)")
                    attempted_problems += 1
                else:
                    print(f"  ❌ {problem_name} (not started)")
                    
            except Exception as e:
                print(f"  ⚠️  {problem_name} (error checking: {e})")
        else:
            print(f"  ❌ {problem_name} (file missing)")
    
    print(f"\nProblems attempted: {attempted_problems}/{len(problems)}")
    return attempted_problems


def run_tests():
    """
    Run tests and show results
    """
    print("\n🧪 Test Results:")
    print("-" * 40)
    
    test_files = [
        ("test_problem_01.py", "API Concepts Tests"),
        ("test_problem_02.py", "HTTP Concepts Tests"),
        ("test_problem_03.py", "First Requests Tests"),
    ]
    
    total_passed = 0
    total_failed = 0
    
    for test_file, test_name in test_files:
        test_path = f"tests/{test_file}"
        if os.path.exists(test_path):
            try:
                # Run pytest for this specific file
                result = subprocess.run([
                    sys.executable, "-m", "pytest", test_path, "-v", "--tb=no"
                ], capture_output=True, text=True, cwd=".")
                
                # Parse results
                output = result.stdout
                if "passed" in output or "failed" in output:
                    lines = output.split('\n')
                    for line in lines:
                        if ' passed' in line or ' failed' in line:
                            # Extract numbers
                            import re
                            passed_match = re.search(r'(\d+) passed', line)
                            failed_match = re.search(r'(\d+) failed', line)
                            
                            passed = int(passed_match.group(1)) if passed_match else 0
                            failed = int(failed_match.group(1)) if failed_match else 0
                            
                            total_passed += passed
                            total_failed += failed
                            
                            if failed == 0 and passed > 0:
                                print(f"  ✅ {test_name}: {passed} passed")
                            elif passed > 0:
                                print(f"  🔄 {test_name}: {passed} passed, {failed} failed")
                            else:
                                print(f"  ❌ {test_name}: {failed} failed")
                            break
                    else:
                        print(f"  ❓ {test_name}: No tests run")
                else:
                    print(f"  ❓ {test_name}: No results")
                    
            except Exception as e:
                print(f"  💥 {test_name}: Error running tests ({e})")
        else:
            print(f"  ❌ {test_name}: Test file missing")
    
    print(f"\nOverall Test Results: {total_passed} passed, {total_failed} failed")
    return total_passed, total_failed


def check_dependencies():
    """
    Check if required dependencies are installed
    """
    print("\n📦 Dependency Check:")
    print("-" * 40)
    
    dependencies = [
        ("requests", "Making HTTP requests"),
        ("pytest", "Running tests"),
        ("json", "JSON handling (built-in)"),
    ]
    
    missing_deps = []
    
    for dep_name, description in dependencies:
        try:
            if dep_name == "json":
                import json
            else:
                __import__(dep_name)
            print(f"  ✅ {dep_name}: {description}")
        except ImportError:
            print(f"  ❌ {dep_name}: {description} (MISSING)")
            missing_deps.append(dep_name)
    
    if missing_deps:
        print(f"\n⚠️  Missing dependencies: {', '.join(missing_deps)}")
        print("Install with: pip install " + " ".join(missing_deps))
    else:
        print("\n✅ All dependencies are installed!")
    
    return len(missing_deps) == 0


def show_next_steps(lessons_completed, problems_attempted, tests_passed):
    """
    Show recommended next steps
    """
    print("\n🎯 Recommended Next Steps:")
    print("-" * 40)
    
    if lessons_completed == 0:
        print("  1. Start with lesson_01_what_are_apis.py")
        print("  2. Read through the lesson content")
        print("  3. Run the lesson to see examples")
    elif lessons_completed < 3:
        next_lesson = lessons_completed + 1
        print(f"  1. Continue with lesson_0{next_lesson}_*.py")
        print("  2. Review previous lessons if needed")
    else:
        print("  ✅ All basic lessons completed!")
    
    if problems_attempted < 1:
        print("  3. Try problem_01_api_concepts.py")
        print("  4. Run tests to check your solutions")
    elif problems_attempted < 3:
        next_problem = int(problems_attempted) + 1
        print(f"  3. Work on problem_0{next_problem}_*.py")
        print("  4. Run tests to verify your solutions")
    else:
        print("  ✅ All basic problems attempted!")
    
    if tests_passed < 10:
        print("  5. Focus on getting more tests to pass")
        print("  6. Review examples/ folder for help")
    else:
        print("  ✅ Great job on the tests!")
        print("  5. Ready for advanced lessons!")


def main():
    """
    Run complete progress check
    """
    print("📊 API Learning Progress Report")
    print("=" * 50)
    
    # Check dependencies first
    deps_ok = check_dependencies()
    
    if not deps_ok:
        print("\n⚠️  Please install missing dependencies before continuing.")
        return
    
    # Check progress
    lessons_completed = check_lesson_completion()
    problems_attempted = check_problem_solutions()
    tests_passed, tests_failed = run_tests()
    
    # Calculate overall progress
    total_progress = (lessons_completed * 20 + problems_attempted * 20 + min(tests_passed, 20) * 3)
    
    print(f"\n📈 Overall Progress: {total_progress:.0f}%")
    print("=" * 50)
    
    # Show next steps
    show_next_steps(lessons_completed, problems_attempted, tests_passed)
    
    print("\n🚀 Keep learning! You're doing great!")


if __name__ == "__main__":
    main()
