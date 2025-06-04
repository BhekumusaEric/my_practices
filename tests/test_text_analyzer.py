"""
Test cases for text_analyzer.py
These tests will help you understand exactly what your functions should do.
"""

import unittest
import sys
import os

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from text_analyzer import analyze_text, find_longest_words, count_vowels_consonants


class TestTextAnalyzer(unittest.TestCase):
    
    def test_analyze_text_basic(self):
        """Test basic text analysis"""
        text = "Hello world! Hello Python. Python is great!"
        result = analyze_text(text)
        
        self.assertEqual(result['word_count'], 6)
        self.assertEqual(result['unique_words'], 5)
        
        expected_freq = {'hello': 2, 'world': 1, 'python': 2, 'is': 1, 'great': 1}
        self.assertEqual(result['word_frequency'], expected_freq)
        
        # Most common word should be either 'hello' or 'python' (both have frequency 2)
        self.assertIn(result['most_common_word'], ['hello', 'python'])
        
        # Average word length: (5+5+5+6+2+5)/6 = 28/6 = 4.67
        self.assertAlmostEqual(result['average_word_length'], 4.67, places=2)
    
    def test_analyze_text_empty_string(self):
        """Test with empty string"""
        result = analyze_text("")
        
        self.assertEqual(result['word_count'], 0)
        self.assertEqual(result['unique_words'], 0)
        self.assertEqual(result['word_frequency'], {})
        self.assertEqual(result['most_common_word'], "")
        self.assertEqual(result['average_word_length'], 0.0)
    
    def test_analyze_text_single_word(self):
        """Test with single word"""
        result = analyze_text("Python")
        
        self.assertEqual(result['word_count'], 1)
        self.assertEqual(result['unique_words'], 1)
        self.assertEqual(result['word_frequency'], {'python': 1})
        self.assertEqual(result['most_common_word'], 'python')
        self.assertEqual(result['average_word_length'], 6.0)
    
    def test_analyze_text_punctuation_removal(self):
        """Test punctuation removal"""
        text = "Hello, world! How are you? I'm fine."
        result = analyze_text(text)
        
        # Should have: hello, world, how, are, you, im, fine (7 words)
        self.assertEqual(result['word_count'], 7)
        self.assertIn('hello', result['word_frequency'])
        self.assertIn('world', result['word_frequency'])
        self.assertIn('im', result['word_frequency'])  # I'm becomes im
    
    def test_analyze_text_case_insensitive(self):
        """Test case insensitivity"""
        text = "Python PYTHON python PyThOn"
        result = analyze_text(text)
        
        self.assertEqual(result['word_count'], 4)
        self.assertEqual(result['unique_words'], 1)
        self.assertEqual(result['word_frequency'], {'python': 4})
        self.assertEqual(result['most_common_word'], 'python')
    
    def test_find_longest_words_basic(self):
        """Test finding longest words"""
        text = "Python programming is challenging and rewarding"
        result = find_longest_words(text, 3)
        
        # Expected: programming(11), challenging(11), rewarding(9)
        # For same length, should be alphabetical
        expected = ['challenging', 'programming', 'rewarding']
        self.assertEqual(result, expected)
    
    def test_find_longest_words_fewer_than_n(self):
        """Test when text has fewer unique words than n"""
        text = "Hello world"
        result = find_longest_words(text, 5)
        
        # Should return both words, longest first
        expected = ['hello', 'world']  # Both length 5, alphabetical order
        self.assertEqual(result, expected)
    
    def test_find_longest_words_empty_text(self):
        """Test with empty text"""
        result = find_longest_words("", 3)
        self.assertEqual(result, [])
    
    def test_find_longest_words_duplicates(self):
        """Test with duplicate words"""
        text = "cat dog elephant cat dog"
        result = find_longest_words(text, 3)
        
        # Should return unique words: elephant(8), cat(3), dog(3)
        expected = ['elephant', 'cat', 'dog']
        self.assertEqual(result, expected)
    
    def test_count_vowels_consonants_basic(self):
        """Test basic vowel/consonant counting"""
        result = count_vowels_consonants("Hello World!")
        
        # H-e-l-l-o W-o-r-l-d
        # Vowels: e, o, o = 3
        # Consonants: H, l, l, W, r, l, d = 7
        self.assertEqual(result['vowels'], 3)
        self.assertEqual(result['consonants'], 7)
    
    def test_count_vowels_consonants_case_insensitive(self):
        """Test case insensitivity"""
        result = count_vowels_consonants("AEIOUaeiou")
        
        # All vowels
        self.assertEqual(result['vowels'], 10)
        self.assertEqual(result['consonants'], 0)
    
    def test_count_vowels_consonants_non_alphabetic(self):
        """Test ignoring non-alphabetic characters"""
        result = count_vowels_consonants("Hello123!@# World456")
        
        # Same as "Hello World" - should ignore numbers and symbols
        self.assertEqual(result['vowels'], 3)
        self.assertEqual(result['consonants'], 7)
    
    def test_count_vowels_consonants_empty_string(self):
        """Test with empty string"""
        result = count_vowels_consonants("")
        
        self.assertEqual(result['vowels'], 0)
        self.assertEqual(result['consonants'], 0)
    
    def test_count_vowels_consonants_only_consonants(self):
        """Test with only consonants"""
        result = count_vowels_consonants("bcdfg")
        
        self.assertEqual(result['vowels'], 0)
        self.assertEqual(result['consonants'], 5)


if __name__ == '__main__':
    unittest.main()
