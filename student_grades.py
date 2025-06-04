"""
Problem 2: Dictionary Management
Understanding of basic data structures - Dictionaries
"""

def calculate_student_stats(grades_dict):
    """
    Calculate statistics from a dictionary of student grades.
    
    Args:
        grades_dict (dict): Dictionary where keys are student names (str) 
                           and values are lists of grades (list of int/float)
                           
    Returns:
        dict: Dictionary with student names as keys and their stats as values.
              Each student's stats should be a dictionary containing:
              - 'average': float (rounded to 2 decimal places)
              - 'highest': int/float
              - 'lowest': int/float
              - 'total_assignments': int
              
    Example:
        grades = {
            'Alice': [85, 92, 78, 96],
            'Bob': [76, 88, 92],
            'Charlie': [95, 87, 91, 89, 93]
        }
        
        Result should be:
        {
            'Alice': {'average': 87.75, 'highest': 96, 'lowest': 78, 'total_assignments': 4},
            'Bob': {'average': 85.33, 'highest': 92, 'lowest': 76, 'total_assignments': 3},
            'Charlie': {'average': 91.0, 'highest': 95, 'lowest': 87, 'total_assignments': 5}
        }
    """
    # TODO: Implement this function
    pass


def get_top_students(grades_dict, n=3):
    """
    Get the top N students based on their average grades.
    
    Args:
        grades_dict (dict): Dictionary of student grades
        n (int): Number of top students to return (default: 3)
        
    Returns:
        list: List of tuples (student_name, average_grade) sorted by average grade (highest first)
        
    Example:
        grades = {
            'Alice': [85, 92, 78, 96],
            'Bob': [76, 88, 92],
            'Charlie': [95, 87, 91, 89, 93]
        }
        get_top_students(grades, 2) -> [('Charlie', 91.0), ('Alice', 87.75)]
    """
    # TODO: Implement this function
    pass


def students_above_threshold(grades_dict, threshold):
    """
    Find students whose average grade is above the given threshold.
    
    Args:
        grades_dict (dict): Dictionary of student grades
        threshold (float): Minimum average grade threshold
        
    Returns:
        list: List of student names whose average is above threshold, sorted alphabetically
        
    Example:
        grades = {
            'Alice': [85, 92, 78, 96],
            'Bob': [76, 88, 92],
            'Charlie': [95, 87, 91, 89, 93]
        }
        students_above_threshold(grades, 90) -> ['Charlie']
    """
    # TODO: Implement this function
    pass
