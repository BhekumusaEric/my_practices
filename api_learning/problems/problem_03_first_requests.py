#!/usr/bin/env python3
"""
Problem 3: Making Your First Requests 🚀

Practice making HTTP requests using the requests library.
Complete the functions to make various types of API calls.
"""

import requests
import json


def get_random_fact():
    """
    Get a random cat fact from the Cat Facts API.
    
    API: https://catfact.ninja/fact
    
    Returns:
        dict: Response containing the fact, or error info
        
    Example return:
        {
            "success": True,
            "fact": "Cats have 32 muscles in each ear.",
            "length": 32
        }
        
    Or on error:
        {
            "success": False,
            "error": "Network error"
        }
    """
    # TODO: Make request to cat facts API
    # Handle errors gracefully
    pass


def get_user_info(user_id):
    """
    Get user information from JSONPlaceholder API.
    
    API: https://jsonplaceholder.typicode.com/users/{user_id}
    
    Args:
        user_id (int): ID of the user to fetch
        
    Returns:
        dict: User information or error
        
    Example return:
        {
            "success": True,
            "user": {
                "id": 1,
                "name": "Leanne Graham",
                "email": "Sincere@april.biz"
            }
        }
    """
    # TODO: Make request to get user info
    # Handle different status codes appropriately
    pass


def get_posts_with_params(user_id=None, limit=None):
    """
    Get posts from JSONPlaceholder with optional parameters.
    
    API: https://jsonplaceholder.typicode.com/posts
    
    Args:
        user_id (int, optional): Filter posts by user ID
        limit (int, optional): Limit number of posts returned
        
    Returns:
        dict: Posts data or error
        
    Example:
        get_posts_with_params(user_id=1, limit=5)
        -> Returns first 5 posts from user 1
    """
    # TODO: Make request with query parameters
    # Use requests params parameter for query string
    pass


def make_request_with_headers(url, custom_headers=None):
    """
    Make a request with custom headers.
    
    Args:
        url (str): URL to make request to
        custom_headers (dict, optional): Custom headers to include
        
    Returns:
        dict: Response info including headers sent and received
        
    Example return:
        {
            "success": True,
            "status_code": 200,
            "headers_sent": {"User-Agent": "MyApp/1.0"},
            "headers_received": {"Content-Type": "application/json"}
        }
    """
    # TODO: Make request with custom headers
    # Return info about both sent and received headers
    pass


def test_different_endpoints():
    """
    Test multiple endpoints and return a summary.
    
    Test these endpoints:
    - https://httpbin.org/status/200 (should return 200)
    - https://httpbin.org/status/404 (should return 404) 
    - https://httpbin.org/delay/1 (should work but be slow)
    
    Returns:
        dict: Summary of all endpoint tests
        
    Example return:
        {
            "results": [
                {"url": "...", "status": 200, "success": True},
                {"url": "...", "status": 404, "success": False},
                {"url": "...", "status": 200, "success": True, "slow": True}
            ]
        }
    """
    # TODO: Test multiple endpoints
    # Use timeout to handle slow requests
    pass


def handle_json_response(url):
    """
    Make a request and properly handle JSON response.
    
    Args:
        url (str): URL that returns JSON
        
    Returns:
        dict: Parsed JSON data or error info
        
    Handle these cases:
    - Successful JSON response
    - Non-JSON response
    - Network errors
    - Invalid JSON
    """
    # TODO: Make request and handle JSON parsing
    # Include proper error handling for JSON parsing
    pass


def make_request_with_timeout(url, timeout_seconds=5):
    """
    Make a request with a specific timeout.
    
    Args:
        url (str): URL to request
        timeout_seconds (int): Timeout in seconds
        
    Returns:
        dict: Response info including timing
        
    Example return:
        {
            "success": True,
            "status_code": 200,
            "response_time": 1.23,
            "timed_out": False
        }
    """
    # TODO: Make request with timeout
    # Measure response time and handle timeout errors
    pass


def compare_response_formats(base_url):
    """
    Compare different response formats from the same API.
    
    Args:
        base_url (str): Base URL (e.g., "https://httpbin.org")
        
    Test these endpoints:
    - /json (returns JSON)
    - /xml (returns XML)
    - /html (returns HTML)
    
    Returns:
        dict: Comparison of different formats
        
    Example return:
        {
            "json": {"content_type": "application/json", "parseable": True},
            "xml": {"content_type": "application/xml", "parseable": False},
            "html": {"content_type": "text/html", "parseable": False}
        }
    """
    # TODO: Test different response formats
    # Check content-type headers and parseability
    pass


# Bonus challenge function
def api_health_checker(urls):
    """
    Check the health of multiple APIs.
    
    Args:
        urls (list): List of URLs to check
        
    Returns:
        dict: Health status of each API
        
    For each URL, check:
    - Is it reachable?
    - What's the response time?
    - What status code does it return?
    
    Example return:
        {
            "https://api1.com": {
                "status": "healthy",
                "response_time": 0.5,
                "status_code": 200
            },
            "https://api2.com": {
                "status": "unhealthy", 
                "error": "Connection timeout"
            }
        }
    """
    # TODO: Implement API health checker
    # This is a bonus challenge - try it if you finish the others!
    pass


# Test your implementations
if __name__ == "__main__":
    print("🧪 Testing your request-making skills...")
    print("Run the tests to see how you did!")
    print("Command: python -m pytest tests/test_problem_03.py -v")
    
    # You can also test individual functions here
    print("\n🔍 Quick test:")
    try:
        result = get_random_fact()
        if result and result.get("success"):
            print(f"✅ Cat fact: {result.get('fact', 'No fact returned')}")
        else:
            print("❌ Failed to get cat fact")
    except Exception as e:
        print(f"💥 Error testing: {e}")
