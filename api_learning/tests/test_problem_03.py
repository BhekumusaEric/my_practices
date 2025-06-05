"""
Tests for Problem 3: Making Your First Requests
"""

import unittest
import sys
import os
from unittest.mock import patch, Mock

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from problems.problem_03_first_requests import (
    get_random_fact, get_user_info, get_posts_with_params,
    make_request_with_headers, test_different_endpoints,
    handle_json_response, make_request_with_timeout,
    compare_response_formats
)


class TestFirstRequests(unittest.TestCase):
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_get_random_fact_success(self, mock_get):
        """Test successful cat fact retrieval"""
        # Mock successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "fact": "Cats have 32 muscles in each ear.",
            "length": 32
        }
        mock_get.return_value = mock_response
        
        result = get_random_fact()
        
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get("success"))
        self.assertIn("fact", result)
        self.assertIn("length", result)
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_get_random_fact_error(self, mock_get):
        """Test cat fact retrieval with error"""
        # Mock network error
        mock_get.side_effect = Exception("Network error")
        
        result = get_random_fact()
        
        self.assertIsInstance(result, dict)
        self.assertFalse(result.get("success"))
        self.assertIn("error", result)
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_get_user_info_success(self, mock_get):
        """Test successful user info retrieval"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 1,
            "name": "Leanne Graham",
            "email": "Sincere@april.biz"
        }
        mock_get.return_value = mock_response
        
        result = get_user_info(1)
        
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get("success"))
        self.assertIn("user", result)
        self.assertEqual(result["user"]["id"], 1)
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_get_user_info_not_found(self, mock_get):
        """Test user info retrieval with 404"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        result = get_user_info(999)
        
        self.assertIsInstance(result, dict)
        self.assertFalse(result.get("success"))
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_get_posts_with_params(self, mock_get):
        """Test posts retrieval with parameters"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"id": 1, "userId": 1, "title": "Test post"}
        ]
        mock_get.return_value = mock_response
        
        result = get_posts_with_params(user_id=1, limit=5)
        
        self.assertIsInstance(result, dict)
        # Check that requests.get was called with params
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        self.assertIn('params', call_args.kwargs)
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_make_request_with_headers(self, mock_get):
        """Test request with custom headers"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}
        mock_get.return_value = mock_response
        
        custom_headers = {"User-Agent": "MyApp/1.0"}
        result = make_request_with_headers("http://example.com", custom_headers)
        
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get("success"))
        self.assertIn("headers_sent", result)
        self.assertIn("headers_received", result)
        
        # Check that headers were passed to requests
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        self.assertIn('headers', call_args.kwargs)
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_test_different_endpoints(self, mock_get):
        """Test multiple endpoint testing"""
        # Mock different responses for different URLs
        def side_effect(url, **kwargs):
            mock_response = Mock()
            if "200" in url:
                mock_response.status_code = 200
            elif "404" in url:
                mock_response.status_code = 404
            else:
                mock_response.status_code = 200
            return mock_response
        
        mock_get.side_effect = side_effect
        
        result = test_different_endpoints()
        
        self.assertIsInstance(result, dict)
        self.assertIn("results", result)
        self.assertIsInstance(result["results"], list)
        self.assertGreaterEqual(len(result["results"]), 3)
        
        # Check result structure
        for endpoint_result in result["results"]:
            self.assertIn("url", endpoint_result)
            self.assertIn("status", endpoint_result)
            self.assertIn("success", endpoint_result)
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_handle_json_response_success(self, mock_get):
        """Test JSON response handling"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response
        
        result = handle_json_response("http://example.com/json")
        
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get("success"))
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_handle_json_response_invalid_json(self, mock_get):
        """Test handling of invalid JSON"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response
        
        result = handle_json_response("http://example.com/invalid")
        
        self.assertIsInstance(result, dict)
        self.assertFalse(result.get("success"))
        self.assertIn("error", result)
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_make_request_with_timeout(self, mock_get):
        """Test request with timeout"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.elapsed.total_seconds.return_value = 1.5
        mock_get.return_value = mock_response
        
        result = make_request_with_timeout("http://example.com", timeout_seconds=5)
        
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get("success"))
        self.assertIn("response_time", result)
        self.assertIn("timed_out", result)
        self.assertFalse(result["timed_out"])
        
        # Check timeout was passed to requests
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        self.assertIn('timeout', call_args.kwargs)
        self.assertEqual(call_args.kwargs['timeout'], 5)
    
    @patch('problems.problem_03_first_requests.requests.get')
    def test_compare_response_formats(self, mock_get):
        """Test response format comparison"""
        def side_effect(url, **kwargs):
            mock_response = Mock()
            mock_response.status_code = 200
            if "json" in url:
                mock_response.headers = {"Content-Type": "application/json"}
            elif "xml" in url:
                mock_response.headers = {"Content-Type": "application/xml"}
            elif "html" in url:
                mock_response.headers = {"Content-Type": "text/html"}
            return mock_response
        
        mock_get.side_effect = side_effect
        
        result = compare_response_formats("https://httpbin.org")
        
        self.assertIsInstance(result, dict)
        self.assertIn("json", result)
        self.assertIn("xml", result)
        self.assertIn("html", result)
        
        # Check structure of each format result
        for format_name, format_result in result.items():
            self.assertIn("content_type", format_result)
            self.assertIn("parseable", format_result)


if __name__ == '__main__':
    unittest.main()
