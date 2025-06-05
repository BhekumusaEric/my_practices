#!/usr/bin/env python3
"""
Problem 1: API Concepts Understanding 🤔

Test your understanding of basic API concepts.
Complete the functions below to demonstrate your knowledge.
"""

def what_is_api():
    """
    Return a simple explanation of what an API is.
    
    Returns:
        str: A one-sentence explanation of what an API is
        
    Example:
        "An API is a way for different applications to communicate with each other"
    """
    # TODO: Write your explanation here
    pass


def list_http_methods():
    """
    Return a list of the main HTTP methods and their purposes.
    
    Returns:
        list: List of tuples (method, purpose)
        
    Example:
        [("GET", "retrieve data"), ("POST", "create data")]
    """
    # TODO: Return list of HTTP methods and their purposes
    pass


def categorize_status_code(status_code):
    """
    Categorize an HTTP status code.
    
    Args:
        status_code (int): HTTP status code
        
    Returns:
        str: Category of the status code
        
    Categories:
        - "success" for 2xx codes
        - "redirect" for 3xx codes  
        - "client_error" for 4xx codes
        - "server_error" for 5xx codes
        - "unknown" for anything else
        
    Examples:
        categorize_status_code(200) -> "success"
        categorize_status_code(404) -> "client_error"
    """
    # TODO: Implement status code categorization
    pass


def explain_api_analogy():
    """
    Complete the restaurant analogy for APIs.
    
    Returns:
        dict: Dictionary mapping API concepts to restaurant elements
        
    Example:
        {
            "client": "customer",
            "server": "kitchen", 
            "api": "waiter",
            "request": "order",
            "response": "food"
        }
    """
    # TODO: Complete the analogy mapping
    pass


def identify_api_examples():
    """
    Identify which of these are examples of API usage.
    
    Returns:
        list: List of strings that represent API usage
        
    Options to choose from:
        - "Checking weather in a mobile app"
        - "Writing code in a text editor"
        - "Social media app showing friend updates"
        - "Calculator doing math"
        - "Maps app showing directions"
        - "Playing a local video file"
        - "Online shopping checking product prices"
        - "Reading a book"
    """
    # TODO: Return list of API usage examples
    pass


def api_benefits():
    """
    List the main benefits of using APIs.
    
    Returns:
        list: List of strings describing API benefits
        
    Should include benefits like reusability, connectivity, etc.
    """
    # TODO: List the main benefits of APIs
    pass


def match_terms_definitions():
    """
    Match API terms with their definitions.
    
    Returns:
        dict: Dictionary mapping terms to definitions
        
    Terms: "endpoint", "payload", "authentication", "rate_limiting"
    
    Definitions:
        - "Controlling how many requests can be made"
        - "Data sent in a request"
        - "Verifying who is making the request"
        - "Specific URL where an API can be accessed"
    """
    # TODO: Match terms with definitions
    pass


def real_world_api_scenarios():
    """
    For each scenario, identify what type of HTTP method would be used.
    
    Returns:
        dict: Dictionary mapping scenarios to HTTP methods
        
    Scenarios:
        - "Getting user profile information"
        - "Creating a new blog post"
        - "Updating user email address"
        - "Deleting a photo"
        - "Searching for products"
    """
    # TODO: Map scenarios to HTTP methods
    pass


# Test your knowledge
if __name__ == "__main__":
    print("🧪 Testing your API concepts knowledge...")
    print("Run the tests to see how you did!")
    print("Command: python -m pytest tests/test_problem_01.py -v")
