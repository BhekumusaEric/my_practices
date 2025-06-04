"""
Test cases for student_grades.py
These tests will help you understand exactly what your functions should do.
"""

import unittest
import sys
import os

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student_grades import calculate_student_stats, get_top_students, students_above_threshold


class TestStudentGrades(unittest.TestCase):
    
    def setUp(self):
        """Set up test data"""
        self.grades = {
            'Alice': [85, 92, 78, 96],
            'Bob': [76, 88, 92],
            'Charlie': [95, 87, 91, 89, 93],
            'Diana': [100, 98, 99]
        }
    
    def test_calculate_student_stats_basic(self):
        """Test basic statistics calculation"""
        result = calculate_student_stats(self.grades)
        
        # Check Alice's stats
        alice_stats = result['Alice']
        self.assertEqual(alice_stats['average'], 87.75)
        self.assertEqual(alice_stats['highest'], 96)
        self.assertEqual(alice_stats['lowest'], 78)
        self.assertEqual(alice_stats['total_assignments'], 4)
        
        # Check Bob's stats
        bob_stats = result['Bob']
        self.assertEqual(bob_stats['average'], 85.33)
        self.assertEqual(bob_stats['highest'], 92)
        self.assertEqual(bob_stats['lowest'], 76)
        self.assertEqual(bob_stats['total_assignments'], 3)
    
    def test_calculate_student_stats_single_grade(self):
        """Test with single grade per student"""
        grades = {'John': [85], 'Jane': [92]}
        result = calculate_student_stats(grades)
        
        self.assertEqual(result['John']['average'], 85.0)
        self.assertEqual(result['John']['highest'], 85)
        self.assertEqual(result['John']['lowest'], 85)
        self.assertEqual(result['John']['total_assignments'], 1)
    
    def test_calculate_student_stats_empty_dict(self):
        """Test with empty grades dictionary"""
        result = calculate_student_stats({})
        self.assertEqual(result, {})
    
    def test_calculate_student_stats_rounding(self):
        """Test proper rounding of averages"""
        grades = {'Test': [85, 86, 87]}  # Average should be 86.0
        result = calculate_student_stats(grades)
        self.assertEqual(result['Test']['average'], 86.0)
        
        grades = {'Test2': [85, 86]}  # Average should be 85.5
        result = calculate_student_stats(grades)
        self.assertEqual(result['Test2']['average'], 85.5)
    
    def test_get_top_students_basic(self):
        """Test getting top students"""
        result = get_top_students(self.grades, 2)
        
        # Should be sorted by average (highest first)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], 'Diana')  # Highest average
        self.assertAlmostEqual(result[0][1], 99.0, places=2)
        
        # Second highest should be Charlie
        self.assertEqual(result[1][0], 'Charlie')
        self.assertAlmostEqual(result[1][1], 91.0, places=2)
    
    def test_get_top_students_default_n(self):
        """Test default parameter for top students"""
        result = get_top_students(self.grades)  # Default n=3
        self.assertEqual(len(result), 3)
        
        # Check order: Diana, Charlie, Alice
        self.assertEqual(result[0][0], 'Diana')
        self.assertEqual(result[1][0], 'Charlie')
        self.assertEqual(result[2][0], 'Alice')
    
    def test_get_top_students_more_than_available(self):
        """Test requesting more students than available"""
        result = get_top_students(self.grades, 10)
        self.assertEqual(len(result), 4)  # Only 4 students available
    
    def test_get_top_students_empty_dict(self):
        """Test with empty grades dictionary"""
        result = get_top_students({}, 3)
        self.assertEqual(result, [])
    
    def test_students_above_threshold_basic(self):
        """Test finding students above threshold"""
        result = students_above_threshold(self.grades, 90)
        
        # Charlie (91.0) and Diana (99.0) should be above 90
        expected = ['Charlie', 'Diana']
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_students_above_threshold_high_threshold(self):
        """Test with high threshold"""
        result = students_above_threshold(self.grades, 95)
        
        # Only Diana (99.0) should be above 95
        self.assertEqual(result, ['Diana'])
    
    def test_students_above_threshold_low_threshold(self):
        """Test with low threshold"""
        result = students_above_threshold(self.grades, 80)
        
        # All students should be above 80
        expected = ['Alice', 'Bob', 'Charlie', 'Diana']
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_students_above_threshold_no_students(self):
        """Test with threshold higher than all averages"""
        result = students_above_threshold(self.grades, 100)
        self.assertEqual(result, [])
    
    def test_students_above_threshold_empty_dict(self):
        """Test with empty grades dictionary"""
        result = students_above_threshold({}, 85)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
