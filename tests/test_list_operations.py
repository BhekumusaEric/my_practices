"""
Test cases for list_operations.py
These tests will help you understand exactly what your functions should do.
"""

import unittest
import sys
import os

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from list_operations import find_duplicates, remove_duplicates_preserve_order, find_common_elements


class TestListOperations(unittest.TestCase):
    
    def test_find_duplicates_basic(self):
        """Test basic duplicate finding"""
        result = find_duplicates([1, 2, 3, 2, 4, 5, 1])
        self.assertEqual(sorted(result), [1, 2])
    
    def test_find_duplicates_no_duplicates(self):
        """Test with no duplicates"""
        result = find_duplicates([1, 2, 3, 4, 5])
        self.assertEqual(result, [])
    
    def test_find_duplicates_empty_list(self):
        """Test with empty list"""
        result = find_duplicates([])
        self.assertEqual(result, [])
    
    def test_find_duplicates_all_same(self):
        """Test with all same elements"""
        result = find_duplicates([5, 5, 5, 5])
        self.assertEqual(result, [5])
    
    def test_find_duplicates_multiple_duplicates(self):
        """Test with multiple different duplicates"""
        result = find_duplicates([1, 2, 3, 1, 2, 4, 5, 3, 6])
        self.assertEqual(sorted(result), [1, 2, 3])
    
    def test_remove_duplicates_preserve_order_basic(self):
        """Test basic duplicate removal with order preservation"""
        result = remove_duplicates_preserve_order([1, 2, 3, 2, 4, 1, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_remove_duplicates_preserve_order_empty(self):
        """Test with empty list"""
        result = remove_duplicates_preserve_order([])
        self.assertEqual(result, [])
    
    def test_remove_duplicates_preserve_order_no_duplicates(self):
        """Test with no duplicates"""
        result = remove_duplicates_preserve_order([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_remove_duplicates_preserve_order_all_same(self):
        """Test with all same elements"""
        result = remove_duplicates_preserve_order([7, 7, 7, 7])
        self.assertEqual(result, [7])
    
    def test_find_common_elements_basic(self):
        """Test basic common elements finding"""
        result = find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
        self.assertEqual(sorted(result), [3, 4])
    
    def test_find_common_elements_no_common(self):
        """Test with no common elements"""
        result = find_common_elements([1, 2], [3, 4])
        self.assertEqual(result, [])
    
    def test_find_common_elements_empty_lists(self):
        """Test with empty lists"""
        result = find_common_elements([], [1, 2, 3])
        self.assertEqual(result, [])
        
        result = find_common_elements([1, 2, 3], [])
        self.assertEqual(result, [])
        
        result = find_common_elements([], [])
        self.assertEqual(result, [])
    
    def test_find_common_elements_with_duplicates(self):
        """Test with duplicates in input lists"""
        result = find_common_elements([1, 2, 2, 3, 4], [2, 3, 3, 5, 6])
        self.assertEqual(sorted(result), [2, 3])
    
    def test_find_common_elements_identical_lists(self):
        """Test with identical lists"""
        result = find_common_elements([1, 2, 3], [1, 2, 3])
        self.assertEqual(sorted(result), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
