"""
Test cases for sorting_algorithms.py
These tests will help you understand exactly what your functions should do.
"""

import unittest
import sys
import os

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, is_sorted


class TestSortingAlgorithms(unittest.TestCase):
    
    def test_bubble_sort_basic(self):
        """Test basic bubble sort"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = bubble_sort(arr)
        expected = [11, 12, 22, 25, 34, 64, 90]
        
        self.assertEqual(result, expected)
        # Ensure original array is not modified
        self.assertEqual(arr, [64, 34, 25, 12, 22, 11, 90])
    
    def test_bubble_sort_empty_list(self):
        """Test bubble sort with empty list"""
        result = bubble_sort([])
        self.assertEqual(result, [])
    
    def test_bubble_sort_single_element(self):
        """Test bubble sort with single element"""
        result = bubble_sort([5])
        self.assertEqual(result, [5])
    
    def test_bubble_sort_already_sorted(self):
        """Test bubble sort with already sorted array"""
        arr = [1, 2, 3, 4, 5]
        result = bubble_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_bubble_sort_reverse_sorted(self):
        """Test bubble sort with reverse sorted array"""
        arr = [5, 4, 3, 2, 1]
        result = bubble_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_bubble_sort_duplicates(self):
        """Test bubble sort with duplicate elements"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = bubble_sort(arr)
        expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
        self.assertEqual(result, expected)
    
    def test_selection_sort_basic(self):
        """Test basic selection sort"""
        arr = [64, 25, 12, 22, 11]
        result = selection_sort(arr)
        expected = [11, 12, 22, 25, 64]
        
        self.assertEqual(result, expected)
        # Ensure original array is not modified
        self.assertEqual(arr, [64, 25, 12, 22, 11])
    
    def test_selection_sort_empty_list(self):
        """Test selection sort with empty list"""
        result = selection_sort([])
        self.assertEqual(result, [])
    
    def test_selection_sort_single_element(self):
        """Test selection sort with single element"""
        result = selection_sort([42])
        self.assertEqual(result, [42])
    
    def test_selection_sort_duplicates(self):
        """Test selection sort with duplicates"""
        arr = [3, 7, 3, 1, 7, 1]
        result = selection_sort(arr)
        expected = [1, 1, 3, 3, 7, 7]
        self.assertEqual(result, expected)
    
    def test_insertion_sort_basic(self):
        """Test basic insertion sort"""
        arr = [12, 11, 13, 5, 6]
        result = insertion_sort(arr)
        expected = [5, 6, 11, 12, 13]
        
        self.assertEqual(result, expected)
        # Ensure original array is not modified
        self.assertEqual(arr, [12, 11, 13, 5, 6])
    
    def test_insertion_sort_empty_list(self):
        """Test insertion sort with empty list"""
        result = insertion_sort([])
        self.assertEqual(result, [])
    
    def test_insertion_sort_single_element(self):
        """Test insertion sort with single element"""
        result = insertion_sort([99])
        self.assertEqual(result, [99])
    
    def test_insertion_sort_already_sorted(self):
        """Test insertion sort with already sorted array"""
        arr = [1, 2, 3, 4, 5]
        result = insertion_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_is_sorted_true_cases(self):
        """Test is_sorted with sorted arrays"""
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([1]))
        self.assertTrue(is_sorted([]))
        self.assertTrue(is_sorted([5, 5, 5, 5]))  # All same elements
        self.assertTrue(is_sorted([1, 1, 2, 3, 3]))  # With duplicates
    
    def test_is_sorted_false_cases(self):
        """Test is_sorted with unsorted arrays"""
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertFalse(is_sorted([5, 4, 3, 2, 1]))
        self.assertFalse(is_sorted([1, 2, 4, 3, 5]))
        self.assertFalse(is_sorted([2, 1]))
    
    def test_sorting_algorithms_consistency(self):
        """Test that all sorting algorithms produce the same result"""
        test_arrays = [
            [64, 34, 25, 12, 22, 11, 90],
            [3, 1, 4, 1, 5, 9, 2, 6, 5],
            [5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5],
            []
        ]
        
        for arr in test_arrays:
            bubble_result = bubble_sort(arr.copy())
            selection_result = selection_sort(arr.copy())
            insertion_result = insertion_sort(arr.copy())
            
            # All algorithms should produce the same sorted result
            self.assertEqual(bubble_result, selection_result)
            self.assertEqual(selection_result, insertion_result)
            
            # Results should be sorted
            self.assertTrue(is_sorted(bubble_result))
            self.assertTrue(is_sorted(selection_result))
            self.assertTrue(is_sorted(insertion_result))
    
    def test_sorting_with_strings(self):
        """Test sorting algorithms work with strings"""
        arr = ['banana', 'apple', 'cherry', 'date']
        
        bubble_result = bubble_sort(arr)
        selection_result = selection_sort(arr)
        insertion_result = insertion_sort(arr)
        
        expected = ['apple', 'banana', 'cherry', 'date']
        
        self.assertEqual(bubble_result, expected)
        self.assertEqual(selection_result, expected)
        self.assertEqual(insertion_result, expected)


if __name__ == '__main__':
    unittest.main()
