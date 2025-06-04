# Python Assessment Practice Guide

## 🎯 Your Mission
Complete all 6 Python problems to demonstrate mastery of:
- **Data Structures**: Lists, dictionaries, sets, tuples
- **Functions**: Writing and using functions effectively
- **Algorithms**: Sorting, searching, mathematical operations
- **Testing**: Understanding and interpreting unit tests

## 📋 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Initialize Git Repository (if not already done)
```bash
git init
git add .
git commit -m "Initial commit - Python assessment setup"
```

### 3. Run Tests to See What Needs to be Done
```bash
python run_tests.py
```
OR
```bash
python -m pytest tests/ -v
```

## 🧪 Understanding the Tests

Each test file shows you EXACTLY what your functions should do:

- **Input**: What parameters your function receives
- **Output**: What your function should return
- **Edge Cases**: Empty lists, single elements, invalid inputs
- **Examples**: Concrete examples with expected results

**💡 Pro Tip**: Read the test cases BEFORE writing your code. They're your specification!

## 📚 Problem Breakdown

### Problem 1: List Operations (`list_operations.py`)
**Skills**: Lists, Sets, Basic algorithms
- `find_duplicates()` - Find duplicate numbers in a list
- `remove_duplicates_preserve_order()` - Remove duplicates keeping order
- `find_common_elements()` - Find common elements between two lists

### Problem 2: Student Grades (`student_grades.py`) 
**Skills**: Dictionaries, Statistical calculations
- `calculate_student_stats()` - Calculate average, min, max for each student
- `get_top_students()` - Rank students by average grade
- `students_above_threshold()` - Filter students above grade threshold

### Problem 3: Text Analysis (`text_analyzer.py`)
**Skills**: String processing, Dictionaries
- `analyze_text()` - Word frequency analysis
- `find_longest_words()` - Find N longest words
- `count_vowels_consonants()` - Count vowels and consonants

### Problem 4: Sorting Algorithms (`sorting_algorithms.py`)
**Skills**: Algorithm implementation
- `bubble_sort()` - Implement bubble sort
- `selection_sort()` - Implement selection sort  
- `insertion_sort()` - Implement insertion sort
- `is_sorted()` - Check if list is sorted

### Problem 5: Data Processing (`data_processor.py`)
**Skills**: Higher-order functions, Functional programming
- `filter_and_transform()` - Filter data then transform it
- `group_by_property()` - Group data by a property
- `apply_operations()` - Apply multiple operations sequentially
- `find_max_by_criteria()` - Find max element by custom criteria

### Problem 6: Math Utils (`math_utils.py`)
**Skills**: Mathematical algorithms, Recursion/iteration
- `fibonacci_sequence()` - Generate Fibonacci numbers
- `is_prime()` - Check if number is prime
- `prime_factors()` - Find prime factors
- `gcd()` - Greatest Common Divisor (Euclidean algorithm)
- `lcm()` - Least Common Multiple

## 🔄 Development Workflow

For EACH function you complete:

1. **Implement** the function
2. **Test** your implementation:
   ```bash
   python -m pytest tests/test_[filename].py -v
   ```
3. **Commit** your work:
   ```bash
   git add [filename].py
   git commit -m "Implement [function_name]"
   git push
   ```

## 🚨 Assessment Rules Reminder

- ✅ Only use https://docs.python.org/3/
- ✅ Use Visual Studio Code
- ❌ No other websites, tabs, or applications
- ❌ No phones, headphones, or books
- ❌ Code with syntax errors = automatic zero
- ⚠️ Must push code to pass

## 🎯 Success Tips

1. **Read tests first** - They tell you exactly what to do
2. **Start simple** - Get basic cases working before edge cases
3. **Test frequently** - Run tests after each small change
4. **Commit often** - Don't lose your work
5. **Handle edge cases** - Empty lists, None values, etc.
6. **Use appropriate data structures** - Sets for uniqueness, dicts for mapping
7. **Don't modify original data** unless specified

## 🔍 Common Patterns

### Working with Lists
```python
# Remove duplicates while preserving order
seen = set()
result = []
for item in original_list:
    if item not in seen:
        seen.add(item)
        result.append(item)
```

### Working with Dictionaries
```python
# Count frequencies
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
```

### Sorting Algorithms Template
```python
def sort_algorithm(arr):
    # Don't modify original array
    arr_copy = arr.copy()
    # Your sorting logic here
    return arr_copy
```

## 🏆 Final Checklist

Before submitting:
- [ ] All tests pass (`python run_tests.py`)
- [ ] No syntax errors
- [ ] All functions implemented (no `pass` statements)
- [ ] Code is committed and pushed
- [ ] Functions handle edge cases (empty inputs, etc.)

Good luck! Remember: the tests are your friend - they show you exactly what success looks like! 🚀
