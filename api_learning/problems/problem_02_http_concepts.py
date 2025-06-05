#!/usr/bin/env python3
"""
Problem 2: HTTP Concepts Practice 🌐

Practice working with HTTP concepts, URLs, headers, and status codes.
"""

def parse_url_components(url):
    """
    Parse a URL into its components.
    
    Args:
        url (str): A complete URL
        
    Returns:
        dict: Dictionary with URL components
        
    Example:
        parse_url_components("https://api.example.com/v1/users?page=2&limit=10")
        -> {
            "protocol": "https",
            "domain": "api.example.com", 
            "path": "/v1/users",
            "parameters": {"page": "2", "limit": "10"}
        }
    """
    # TODO: Parse URL into components
    # Hint: You can use urllib.parse or do it manually
    pass


def build_request_headers(content_type=None, auth_token=None, user_agent=None):
    """
    Build HTTP request headers dictionary.
    
    Args:
        content_type (str, optional): Content type for the request
        auth_token (str, optional): Authorization token
        user_agent (str, optional): User agent string
        
    Returns:
        dict: Headers dictionary
        
    Example:
        build_request_headers("application/json", "abc123", "MyApp/1.0")
        -> {
            "Content-Type": "application/json",
            "Authorization": "Bearer abc123", 
            "User-Agent": "MyApp/1.0"
        }
    """
    # TODO: Build headers dictionary
    pass


def determine_http_method(action):
    """
    Determine the appropriate HTTP method for different actions.
    
    Args:
        action (str): Description of the action
        
    Returns:
        str: HTTP method (GET, POST, PUT, DELETE, PATCH)
        
    Examples:
        determine_http_method("get user profile") -> "GET"
        determine_http_method("create new account") -> "POST"
        determine_http_method("update email address") -> "PUT" or "PATCH"
        determine_http_method("remove user") -> "DELETE"
    """
    # TODO: Map actions to HTTP methods
    pass


def interpret_status_code(status_code):
    """
    Interpret what an HTTP status code means.
    
    Args:
        status_code (int): HTTP status code
        
    Returns:
        dict: Information about the status code
        
    Example:
        interpret_status_code(404)
        -> {
            "category": "client_error",
            "meaning": "Not Found",
            "description": "The requested resource was not found"
        }
    """
    # TODO: Interpret status codes
    # Include at least: 200, 201, 400, 401, 404, 500
    pass


def build_query_string(params):
    """
    Build a query string from parameters dictionary.
    
    Args:
        params (dict): Parameters to include in query string
        
    Returns:
        str: Query string (without leading ?)
        
    Example:
        build_query_string({"page": 2, "limit": 10, "sort": "name"})
        -> "page=2&limit=10&sort=name"
    """
    # TODO: Build query string from parameters
    pass


def validate_http_method(method):
    """
    Check if a string is a valid HTTP method.
    
    Args:
        method (str): HTTP method to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Valid methods: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS
    """
    # TODO: Validate HTTP method
    pass


def categorize_headers(headers):
    """
    Categorize headers by their purpose.
    
    Args:
        headers (dict): Dictionary of headers
        
    Returns:
        dict: Headers categorized by purpose
        
    Categories:
        - "authentication": Headers related to auth
        - "content": Headers about content type/encoding
        - "caching": Headers about caching
        - "other": Everything else
        
    Example:
        categorize_headers({
            "Authorization": "Bearer token",
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "User-Agent": "MyApp"
        })
        -> {
            "authentication": ["Authorization"],
            "content": ["Content-Type"],
            "caching": ["Cache-Control"], 
            "other": ["User-Agent"]
        }
    """
    # TODO: Categorize headers by purpose
    pass


def create_rest_endpoints(resource):
    """
    Create RESTful endpoints for a given resource.
    
    Args:
        resource (str): Name of the resource (e.g., "users", "posts")
        
    Returns:
        dict: Dictionary mapping operations to endpoints
        
    Example:
        create_rest_endpoints("users")
        -> {
            "list_all": "GET /users",
            "get_one": "GET /users/{id}",
            "create": "POST /users",
            "update": "PUT /users/{id}",
            "delete": "DELETE /users/{id}"
        }
    """
    # TODO: Create RESTful endpoints
    pass


# Test your knowledge
if __name__ == "__main__":
    print("🧪 Testing your HTTP concepts knowledge...")
    print("Run the tests to see how you did!")
    print("Command: python -m pytest tests/test_problem_02.py -v")
