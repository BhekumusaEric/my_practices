"""
Tests for Problem 1: API Concepts Understanding
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from problems.problem_01_api_concepts import (
    what_is_api, list_http_methods, categorize_status_code,
    explain_api_analogy, identify_api_examples, api_benefits,
    match_terms_definitions, real_world_api_scenarios
)


class TestAPIConcepts(unittest.TestCase):
    
    def test_what_is_api(self):
        """Test API definition"""
        result = what_is_api()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)
        # Should mention communication or interface
        self.assertTrue(any(word in result.lower() for word in ['communicate', 'interface', 'connect']))
    
    def test_list_http_methods(self):
        """Test HTTP methods listing"""
        result = list_http_methods()
        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 4)  # At least GET, POST, PUT, DELETE
        
        # Check structure
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
            method, purpose = item
            self.assertIsInstance(method, str)
            self.assertIsInstance(purpose, str)
        
        # Check for main methods
        methods = [item[0].upper() for item in result]
        self.assertIn('GET', methods)
        self.assertIn('POST', methods)
    
    def test_categorize_status_code(self):
        """Test status code categorization"""
        # Test success codes
        self.assertEqual(categorize_status_code(200), "success")
        self.assertEqual(categorize_status_code(201), "success")
        
        # Test redirect codes
        self.assertEqual(categorize_status_code(301), "redirect")
        self.assertEqual(categorize_status_code(302), "redirect")
        
        # Test client error codes
        self.assertEqual(categorize_status_code(400), "client_error")
        self.assertEqual(categorize_status_code(404), "client_error")
        
        # Test server error codes
        self.assertEqual(categorize_status_code(500), "server_error")
        self.assertEqual(categorize_status_code(503), "server_error")
        
        # Test unknown codes
        self.assertEqual(categorize_status_code(100), "unknown")
        self.assertEqual(categorize_status_code(600), "unknown")
    
    def test_explain_api_analogy(self):
        """Test restaurant analogy"""
        result = explain_api_analogy()
        self.assertIsInstance(result, dict)
        
        required_keys = ["client", "server", "api", "request", "response"]
        for key in required_keys:
            self.assertIn(key, result)
            self.assertIsInstance(result[key], str)
        
        # Check for reasonable analogies
        self.assertIn("customer", result["client"].lower())
        self.assertIn("kitchen", result["server"].lower())
        self.assertIn("waiter", result["api"].lower())
    
    def test_identify_api_examples(self):
        """Test API example identification"""
        result = identify_api_examples()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        
        # Should include these API examples
        api_examples = [
            "Checking weather in a mobile app",
            "Social media app showing friend updates", 
            "Maps app showing directions",
            "Online shopping checking product prices"
        ]
        
        for example in api_examples:
            self.assertIn(example, result)
        
        # Should NOT include these non-API examples
        non_api_examples = [
            "Writing code in a text editor",
            "Calculator doing math",
            "Playing a local video file",
            "Reading a book"
        ]
        
        for example in non_api_examples:
            self.assertNotIn(example, result)
    
    def test_api_benefits(self):
        """Test API benefits listing"""
        result = api_benefits()
        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 3)
        
        # Should mention key benefits
        benefits_text = " ".join(result).lower()
        benefit_keywords = ['reuse', 'connect', 'scale', 'integrate', 'efficiency']
        
        found_keywords = sum(1 for keyword in benefit_keywords if keyword in benefits_text)
        self.assertGreaterEqual(found_keywords, 2)
    
    def test_match_terms_definitions(self):
        """Test term-definition matching"""
        result = match_terms_definitions()
        self.assertIsInstance(result, dict)
        
        required_terms = ["endpoint", "payload", "authentication", "rate_limiting"]
        for term in required_terms:
            self.assertIn(term, result)
            self.assertIsInstance(result[term], str)
        
        # Check for reasonable definitions
        self.assertIn("url", result["endpoint"].lower())
        self.assertIn("data", result["payload"].lower())
        self.assertIn("who", result["authentication"].lower())
        self.assertIn("request", result["rate_limiting"].lower())
    
    def test_real_world_api_scenarios(self):
        """Test HTTP method scenarios"""
        result = real_world_api_scenarios()
        self.assertIsInstance(result, dict)
        
        # Check expected mappings
        expected_mappings = {
            "Getting user profile information": "GET",
            "Creating a new blog post": "POST", 
            "Deleting a photo": "DELETE",
            "Searching for products": "GET"
        }
        
        for scenario, expected_method in expected_mappings.items():
            self.assertIn(scenario, result)
            self.assertEqual(result[scenario].upper(), expected_method)


if __name__ == '__main__':
    unittest.main()
