"""
Problem 3: Text Analysis
String processing and dictionary operations
"""

def analyze_text(text):
    """
    Analyze text and return word frequency statistics.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Dictionary containing:
              - 'word_count': int (total number of words)
              - 'unique_words': int (number of unique words)
              - 'word_frequency': dict (word -> frequency mapping)
              - 'most_common_word': str (most frequent word, lowercase)
              - 'average_word_length': float (rounded to 2 decimal places)
              
    Notes:
        - Words should be converted to lowercase
        - Remove punctuation (.,!?;:) from words
        - Split on whitespace
        - Empty strings should return appropriate zero values
        
    Example:
        text = "Hello world! Hello Python. Python is great!"
        Result:
        {
            'word_count': 6,
            'unique_words': 5,
            'word_frequency': {'hello': 2, 'world': 1, 'python': 2, 'is': 1, 'great': 1},
            'most_common_word': 'hello',  # or 'python' (both have frequency 2)
            'average_word_length': 5.17
        }
    """
    # TODO: Implement this function
    pass


def find_longest_words(text, n=3):
    """
    Find the N longest unique words in the text.
    
    Args:
        text (str): Input text
        n (int): Number of longest words to return
        
    Returns:
        list: List of the N longest unique words, sorted by length (descending), 
              then alphabetically for words of same length
              
    Example:
        text = "Python programming is challenging and rewarding"
        find_longest_words(text, 3) -> ['programming', 'challenging', 'rewarding']
    """
    # TODO: Implement this function
    pass


def count_vowels_consonants(text):
    """
    Count vowels and consonants in the text.
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary with 'vowels' and 'consonants' counts
              Only count alphabetic characters, ignore case
              
    Example:
        count_vowels_consonants("Hello World!") -> {'vowels': 3, 'consonants': 7}
    """
    # TODO: Implement this function
    pass
