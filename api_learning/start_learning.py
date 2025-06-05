#!/usr/bin/env python3
"""
API Learning Quick Start 🚀

Your entry point to learning APIs from the ground up!
"""

import os
import sys
import subprocess


def welcome_message():
    """
    Display welcome message and overview
    """
    print("🚀 Welcome to API Learning!")
    print("=" * 50)
    print()
    print("This comprehensive course will teach you:")
    print("  📖 What APIs are and why they matter")
    print("  🌐 HTTP fundamentals and web communication")
    print("  🐍 Making API calls with Python")
    print("  🔧 Building your own APIs")
    print("  🛡️  Security and best practices")
    print()
    print("📚 Learning Structure:")
    print("  • Lessons: Step-by-step tutorials")
    print("  • Problems: Hands-on coding challenges")
    print("  • Tests: Verify your understanding")
    print("  • Examples: Working code to study")
    print("  • Projects: Real-world applications")


def check_setup():
    """
    Check if everything is set up correctly
    """
    print("\n🔍 Checking Setup...")
    print("-" * 30)
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 7:
        print(f"  ✅ Python {python_version.major}.{python_version.minor}")
    else:
        print(f"  ⚠️  Python {python_version.major}.{python_version.minor} (recommend 3.7+)")
    
    # Check required packages
    required_packages = ['requests', 'pytest']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package} installed")
        except ImportError:
            print(f"  ❌ {package} missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📦 Install missing packages:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    
    return True


def show_learning_path():
    """
    Show the recommended learning path
    """
    print("\n🛤️  Your Learning Path:")
    print("-" * 30)
    
    path = [
        ("1️⃣", "lesson_01_what_are_apis.py", "Understand what APIs are"),
        ("2️⃣", "lesson_02_http_basics.py", "Learn HTTP fundamentals"),
        ("3️⃣", "lesson_03_first_api_call.py", "Make your first API call"),
        ("🧪", "problem_01_api_concepts.py", "Test your knowledge"),
        ("🧪", "problem_02_http_concepts.py", "Practice HTTP concepts"),
        ("🧪", "problem_03_first_requests.py", "Code real API calls"),
    ]
    
    for step, filename, description in path:
        print(f"  {step} {filename}")
        print(f"     {description}")
        print()


def run_first_lesson():
    """
    Offer to run the first lesson
    """
    print("🎓 Ready to Start Learning?")
    print("-" * 30)
    
    choice = input("Would you like to run the first lesson now? (y/n): ").lower().strip()
    
    if choice in ['y', 'yes']:
        print("\n🚀 Starting Lesson 1...")
        try:
            # Run the first lesson
            result = subprocess.run([
                sys.executable, "lessons/lesson_01_what_are_apis.py"
            ], cwd=".")
            
            if result.returncode == 0:
                print("\n✅ Lesson 1 completed!")
                print("Next: Run lesson_02_http_basics.py")
            else:
                print("\n⚠️  Lesson had some issues, but that's okay!")
                
        except Exception as e:
            print(f"\n💥 Error running lesson: {e}")
            print("Try running it manually: python lessons/lesson_01_what_are_apis.py")
    else:
        print("\n👍 No problem! Start when you're ready.")


def show_helpful_commands():
    """
    Show useful commands for learning
    """
    print("\n💡 Helpful Commands:")
    print("-" * 30)
    
    commands = [
        ("Run a lesson:", "python lessons/lesson_01_what_are_apis.py"),
        ("Check progress:", "python check_progress.py"),
        ("Run tests:", "python -m pytest tests/ -v"),
        ("See examples:", "python examples/basic_requests_example.py"),
        ("Test one problem:", "python -m pytest tests/test_problem_01.py -v"),
    ]
    
    for description, command in commands:
        print(f"  {description}")
        print(f"    {command}")
        print()


def show_resources():
    """
    Show additional learning resources
    """
    print("📚 Additional Resources:")
    print("-" * 30)
    print("  🌐 Python requests docs: https://docs.python-requests.org/")
    print("  📖 HTTP status codes: https://httpstatuses.com/")
    print("  🔧 Test APIs: https://httpbin.org/")
    print("  📰 Free APIs: https://github.com/public-apis/public-apis")
    print("  🎯 REST API guide: https://restfulapi.net/")


def main():
    """
    Main quick start function
    """
    welcome_message()
    
    setup_ok = check_setup()
    
    if not setup_ok:
        print("\n⚠️  Please install missing packages first, then run this script again.")
        return
    
    show_learning_path()
    show_helpful_commands()
    show_resources()
    
    run_first_lesson()
    
    print("\n" + "=" * 50)
    print("🎉 Happy Learning!")
    print("Remember: Practice makes perfect. Don't rush - understand each concept!")
    print("=" * 50)


if __name__ == "__main__":
    main()
