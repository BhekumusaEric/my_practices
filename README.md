# Python Fundamentals Assessment Practice

## Learning Outcomes
By completing this assessment, you should demonstrate:
- Understanding of basic data structures (lists, dictionaries, tuples, sets)
- Ability to write and use functions
- Problem-solving using simple algorithms
- Ability to write and interpret unit tests

## Instructions
1. Complete each function in the respective Python files
2. Run the tests to verify your solutions
3. For each completed function, you must:
   - `git add`
   - `git commit`
   - `git push`

## Problems Overview

### Problem 1: List Operations (`list_operations.py`)
- **Function**: `find_duplicates(numbers)`
- **Description**: Find all duplicate numbers in a list
- **Data Structure Focus**: Lists, Sets

### Problem 2: Dictionary Management (`student_grades.py`)
- **Function**: `calculate_student_stats(grades_dict)`
- **Description**: Calculate statistics from student grades dictionary
- **Data Structure Focus**: Dictionaries

### Problem 3: String Processing (`text_analyzer.py`)
- **Function**: `analyze_text(text)`
- **Description**: Analyze text and return word frequency statistics
- **Data Structure Focus**: Dictionaries, String manipulation

### Problem 4: Algorithm Implementation (`sorting_algorithms.py`)
- **Function**: `bubble_sort(arr)`
- **Description**: Implement bubble sort algorithm
- **Algorithm Focus**: Sorting algorithms

### Problem 5: Data Filtering (`data_processor.py`)
- **Function**: `filter_and_transform(data, condition_func, transform_func)`
- **Description**: Filter and transform data using higher-order functions
- **Function Focus**: Higher-order functions, lambda expressions

### Problem 6: Mathematical Operations (`math_utils.py`)
- **Function**: `fibonacci_sequence(n)`
- **Description**: Generate Fibonacci sequence up to n terms
- **Algorithm Focus**: Recursive/iterative algorithms

## Running Tests
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_list_operations.py -v
```

## Test Files
- `tests/test_list_operations.py`
- `tests/test_student_grades.py`
- `tests/test_text_analyzer.py`
- `tests/test_sorting_algorithms.py`
- `tests/test_data_processor.py`
- `tests/test_math_utils.py`

## Grading Criteria
- Correct implementation (60%)
- Code quality and readability (20%)
- Proper use of data structures (20%)

**Note**: Code with syntax errors will result in automatic failure.
