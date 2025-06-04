"""
Test cases for data_processor.py
These tests will help you understand exactly what your functions should do.
"""

import unittest
import sys
import os

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_processor import filter_and_transform, group_by_property, apply_operations, find_max_by_criteria


class TestDataProcessor(unittest.TestCase):
    
    def test_filter_and_transform_basic(self):
        """Test basic filter and transform"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Filter even numbers and square them
        result = filter_and_transform(data, lambda x: x % 2 == 0, lambda x: x ** 2)
        expected = [4, 16, 36, 64, 100]  # 2^2, 4^2, 6^2, 8^2, 10^2
        
        self.assertEqual(result, expected)
    
    def test_filter_and_transform_empty_list(self):
        """Test with empty list"""
        result = filter_and_transform([], lambda x: x > 0, lambda x: x * 2)
        self.assertEqual(result, [])
    
    def test_filter_and_transform_no_matches(self):
        """Test when no elements match the condition"""
        data = [1, 3, 5, 7, 9]
        result = filter_and_transform(data, lambda x: x % 2 == 0, lambda x: x * 2)
        self.assertEqual(result, [])
    
    def test_filter_and_transform_all_match(self):
        """Test when all elements match the condition"""
        data = [2, 4, 6, 8]
        result = filter_and_transform(data, lambda x: x % 2 == 0, lambda x: x + 1)
        expected = [3, 5, 7, 9]
        self.assertEqual(result, expected)
    
    def test_filter_and_transform_strings(self):
        """Test with string data"""
        data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        # Filter words longer than 5 chars and convert to uppercase
        result = filter_and_transform(data, lambda x: len(x) > 5, lambda x: x.upper())
        expected = ['BANANA', 'CHERRY', 'ELDERBERRY']
        self.assertEqual(result, expected)
    
    def test_group_by_property_basic(self):
        """Test basic grouping by property"""
        data = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']
        # Group by first letter
        result = group_by_property(data, lambda x: x[0])
        expected = {
            'a': ['apple', 'apricot'],
            'b': ['banana', 'blueberry'],
            'c': ['cherry']
        }
        self.assertEqual(result, expected)
    
    def test_group_by_property_numbers(self):
        """Test grouping numbers by property"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Group by even/odd
        result = group_by_property(data, lambda x: 'even' if x % 2 == 0 else 'odd')
        expected = {
            'odd': [1, 3, 5, 7, 9],
            'even': [2, 4, 6, 8, 10]
        }
        self.assertEqual(result, expected)
    
    def test_group_by_property_empty_list(self):
        """Test with empty list"""
        result = group_by_property([], lambda x: x)
        self.assertEqual(result, {})
    
    def test_group_by_property_length(self):
        """Test grouping by string length"""
        data = ['cat', 'dog', 'elephant', 'ant', 'butterfly']
        result = group_by_property(data, len)
        expected = {
            3: ['cat', 'dog', 'ant'],
            8: ['elephant'],
            9: ['butterfly']
        }
        self.assertEqual(result, expected)
    
    def test_apply_operations_basic(self):
        """Test applying multiple operations"""
        numbers = [1, 2, 3, 4, 5]
        operations = [lambda x: x * 2, lambda x: x + 1]
        # First multiply by 2: [2, 4, 6, 8, 10]
        # Then add 1: [3, 5, 7, 9, 11]
        result = apply_operations(numbers, operations)
        expected = [3, 5, 7, 9, 11]
        self.assertEqual(result, expected)
    
    def test_apply_operations_single_operation(self):
        """Test with single operation"""
        numbers = [1, 2, 3, 4, 5]
        operations = [lambda x: x ** 2]
        result = apply_operations(numbers, operations)
        expected = [1, 4, 9, 16, 25]
        self.assertEqual(result, expected)
    
    def test_apply_operations_no_operations(self):
        """Test with no operations"""
        numbers = [1, 2, 3, 4, 5]
        operations = []
        result = apply_operations(numbers, operations)
        expected = [1, 2, 3, 4, 5]  # Should return original numbers
        self.assertEqual(result, expected)
    
    def test_apply_operations_empty_list(self):
        """Test with empty numbers list"""
        numbers = []
        operations = [lambda x: x * 2, lambda x: x + 1]
        result = apply_operations(numbers, operations)
        self.assertEqual(result, [])
    
    def test_apply_operations_three_operations(self):
        """Test with three operations"""
        numbers = [1, 2, 3]
        operations = [
            lambda x: x * 2,    # [2, 4, 6]
            lambda x: x + 1,    # [3, 5, 7]
            lambda x: x ** 2    # [9, 25, 49]
        ]
        result = apply_operations(numbers, operations)
        expected = [9, 25, 49]
        self.assertEqual(result, expected)
    
    def test_find_max_by_criteria_basic(self):
        """Test finding max by criteria"""
        data = ['apple', 'banana', 'cherry']
        # Find longest string
        result = find_max_by_criteria(data, len)
        self.assertEqual(result, 'banana')  # Length 6
    
    def test_find_max_by_criteria_numbers(self):
        """Test with numbers and custom criteria"""
        data = [1, -5, 3, -2, 4]
        # Find number with maximum absolute value
        result = find_max_by_criteria(data, abs)
        self.assertEqual(result, -5)  # abs(-5) = 5 is maximum
    
    def test_find_max_by_criteria_empty_list(self):
        """Test with empty list"""
        result = find_max_by_criteria([], len)
        self.assertIsNone(result)
    
    def test_find_max_by_criteria_single_element(self):
        """Test with single element"""
        result = find_max_by_criteria(['hello'], len)
        self.assertEqual(result, 'hello')
    
    def test_find_max_by_criteria_tie(self):
        """Test when multiple elements have same max criteria value"""
        data = ['cat', 'dog', 'ant']  # All length 3
        result = find_max_by_criteria(data, len)
        # Should return the first one encountered with max value
        self.assertEqual(result, 'cat')
    
    def test_find_max_by_criteria_complex(self):
        """Test with complex criteria function"""
        data = [
            {'name': 'Alice', 'score': 85},
            {'name': 'Bob', 'score': 92},
            {'name': 'Charlie', 'score': 78}
        ]
        # Find person with highest score
        result = find_max_by_criteria(data, lambda x: x['score'])
        expected = {'name': 'Bob', 'score': 92}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
