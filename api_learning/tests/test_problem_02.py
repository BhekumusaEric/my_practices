"""
Tests for Problem 2: HTTP Concepts Practice
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from problems.problem_02_http_concepts import (
    parse_url_components, build_request_headers, determine_http_method,
    interpret_status_code, build_query_string, validate_http_method,
    categorize_headers, create_rest_endpoints
)


class TestHTTPConcepts(unittest.TestCase):
    
    def test_parse_url_components(self):
        """Test URL parsing"""
        url = "https://api.example.com/v1/users?page=2&limit=10"
        result = parse_url_components(url)
        
        self.assertIsInstance(result, dict)
        self.assertEqual(result["protocol"], "https")
        self.assertEqual(result["domain"], "api.example.com")
        self.assertEqual(result["path"], "/v1/users")
        self.assertIsInstance(result["parameters"], dict)
        self.assertEqual(result["parameters"]["page"], "2")
        self.assertEqual(result["parameters"]["limit"], "10")
    
    def test_build_request_headers(self):
        """Test header building"""
        # Test with all parameters
        result = build_request_headers(
            content_type="application/json",
            auth_token="abc123", 
            user_agent="MyApp/1.0"
        )
        
        self.assertIsInstance(result, dict)
        self.assertEqual(result["Content-Type"], "application/json")
        self.assertEqual(result["Authorization"], "Bearer abc123")
        self.assertEqual(result["User-Agent"], "MyApp/1.0")
        
        # Test with no parameters
        result_empty = build_request_headers()
        self.assertIsInstance(result_empty, dict)
        
        # Test with partial parameters
        result_partial = build_request_headers(content_type="text/plain")
        self.assertEqual(result_partial["Content-Type"], "text/plain")
        self.assertNotIn("Authorization", result_partial)
    
    def test_determine_http_method(self):
        """Test HTTP method determination"""
        test_cases = [
            ("get user profile", "GET"),
            ("retrieve data", "GET"),
            ("create new account", "POST"),
            ("add new item", "POST"),
            ("update email address", ["PUT", "PATCH"]),  # Either is acceptable
            ("modify user", ["PUT", "PATCH"]),
            ("remove user", "DELETE"),
            ("delete item", "DELETE")
        ]
        
        for action, expected in test_cases:
            result = determine_http_method(action)
            if isinstance(expected, list):
                self.assertIn(result.upper(), expected)
            else:
                self.assertEqual(result.upper(), expected)
    
    def test_interpret_status_code(self):
        """Test status code interpretation"""
        # Test 200 OK
        result_200 = interpret_status_code(200)
        self.assertIsInstance(result_200, dict)
        self.assertEqual(result_200["category"], "success")
        self.assertIn("ok", result_200["meaning"].lower())
        
        # Test 404 Not Found
        result_404 = interpret_status_code(404)
        self.assertEqual(result_404["category"], "client_error")
        self.assertIn("not found", result_404["meaning"].lower())
        
        # Test 500 Internal Server Error
        result_500 = interpret_status_code(500)
        self.assertEqual(result_500["category"], "server_error")
        self.assertIn("server", result_500["meaning"].lower())
        
        # Test 201 Created
        result_201 = interpret_status_code(201)
        self.assertEqual(result_201["category"], "success")
        self.assertIn("created", result_201["meaning"].lower())
    
    def test_build_query_string(self):
        """Test query string building"""
        params = {"page": 2, "limit": 10, "sort": "name"}
        result = build_query_string(params)
        
        self.assertIsInstance(result, str)
        self.assertNotStartsWith(result, "?")  # Should not include leading ?
        
        # Should contain all parameters
        self.assertIn("page=2", result)
        self.assertIn("limit=10", result)
        self.assertIn("sort=name", result)
        self.assertIn("&", result)  # Should have separators
        
        # Test empty params
        empty_result = build_query_string({})
        self.assertEqual(empty_result, "")
    
    def assertNotStartsWith(self, text, prefix):
        """Helper method to check text doesn't start with prefix"""
        self.assertFalse(text.startswith(prefix), f"'{text}' should not start with '{prefix}'")
    
    def test_validate_http_method(self):
        """Test HTTP method validation"""
        valid_methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"]
        invalid_methods = ["INVALID", "FETCH", "SEND", ""]
        
        for method in valid_methods:
            self.assertTrue(validate_http_method(method))
            self.assertTrue(validate_http_method(method.lower()))  # Case insensitive
        
        for method in invalid_methods:
            self.assertFalse(validate_http_method(method))
    
    def test_categorize_headers(self):
        """Test header categorization"""
        headers = {
            "Authorization": "Bearer token",
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "User-Agent": "MyApp",
            "Content-Encoding": "gzip",
            "API-Key": "secret"
        }
        
        result = categorize_headers(headers)
        self.assertIsInstance(result, dict)
        
        # Check categories exist
        expected_categories = ["authentication", "content", "caching", "other"]
        for category in expected_categories:
            self.assertIn(category, result)
            self.assertIsInstance(result[category], list)
        
        # Check specific categorizations
        self.assertIn("Authorization", result["authentication"])
        self.assertIn("Content-Type", result["content"])
        self.assertIn("Cache-Control", result["caching"])
        self.assertIn("User-Agent", result["other"])
    
    def test_create_rest_endpoints(self):
        """Test REST endpoint creation"""
        result = create_rest_endpoints("users")
        
        self.assertIsInstance(result, dict)
        
        expected_operations = ["list_all", "get_one", "create", "update", "delete"]
        for operation in expected_operations:
            self.assertIn(operation, result)
            self.assertIsInstance(result[operation], str)
        
        # Check endpoint formats
        self.assertTrue(result["list_all"].startswith("GET /users"))
        self.assertIn("GET /users/{id}", result["get_one"])
        self.assertTrue(result["create"].startswith("POST /users"))
        self.assertIn("PUT /users/{id}", result["update"])
        self.assertIn("DELETE /users/{id}", result["delete"])


if __name__ == '__main__':
    unittest.main()
