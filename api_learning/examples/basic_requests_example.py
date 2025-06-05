#!/usr/bin/env python3
"""
Example: Basic API Requests 📡

This file shows working examples of making API requests.
Study these examples to understand how to use the requests library.
"""

import requests
import json
import time


def example_simple_get():
    """
    Example 1: Simple GET request
    """
    print("🔍 Example 1: Simple GET Request")
    print("-" * 40)
    
    try:
        # Make a simple GET request
        response = requests.get("https://httpbin.org/json")
        
        print(f"Status Code: {response.status_code}")
        print(f"Content Type: {response.headers.get('Content-Type')}")
        print(f"Response Time: {response.elapsed.total_seconds():.2f} seconds")
        
        # Get JSON data
        data = response.json()
        print("Response Data:")
        print(json.dumps(data, indent=2))
        
    except Exception as e:
        print(f"Error: {e}")


def example_get_with_parameters():
    """
    Example 2: GET request with query parameters
    """
    print("\n🔍 Example 2: GET with Parameters")
    print("-" * 40)
    
    try:
        # Parameters as dictionary
        params = {
            'page': 1,
            'per_page': 5,
            'delay': 1
        }
        
        response = requests.get("https://httpbin.org/get", params=params)
        
        print(f"Final URL: {response.url}")
        print(f"Status Code: {response.status_code}")
        
        data = response.json()
        print("Query parameters received by server:")
        print(json.dumps(data['args'], indent=2))
        
    except Exception as e:
        print(f"Error: {e}")


def example_custom_headers():
    """
    Example 3: Request with custom headers
    """
    print("\n🔍 Example 3: Custom Headers")
    print("-" * 40)
    
    try:
        headers = {
            'User-Agent': 'MyAPILearningApp/1.0',
            'Accept': 'application/json',
            'X-Custom-Header': 'Learning APIs'
        }
        
        response = requests.get("https://httpbin.org/headers", headers=headers)
        
        print(f"Status Code: {response.status_code}")
        
        data = response.json()
        print("Headers sent to server:")
        for header, value in data['headers'].items():
            print(f"  {header}: {value}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_error_handling():
    """
    Example 4: Proper error handling
    """
    print("\n🔍 Example 4: Error Handling")
    print("-" * 40)
    
    urls_to_test = [
        ("https://httpbin.org/status/200", "Success case"),
        ("https://httpbin.org/status/404", "Not found case"),
        ("https://httpbin.org/status/500", "Server error case"),
        ("https://invalid-url-that-does-not-exist.com", "Network error case")
    ]
    
    for url, description in urls_to_test:
        print(f"\nTesting: {description}")
        try:
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print("✅ Success!")
            elif response.status_code == 404:
                print("❌ Resource not found")
            elif response.status_code >= 500:
                print("💥 Server error")
            else:
                print(f"⚠️  Unexpected status: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print("⏰ Request timed out")
        except requests.exceptions.ConnectionError:
            print("🌐 Connection error")
        except requests.exceptions.RequestException as e:
            print(f"💥 Request error: {e}")


def example_json_handling():
    """
    Example 5: JSON response handling
    """
    print("\n🔍 Example 5: JSON Handling")
    print("-" * 40)
    
    try:
        # Get some sample JSON data
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")
        
        if response.status_code == 200:
            # Parse JSON
            user_data = response.json()
            
            print("User Information:")
            print(f"  Name: {user_data['name']}")
            print(f"  Email: {user_data['email']}")
            print(f"  Phone: {user_data['phone']}")
            print(f"  Website: {user_data['website']}")
            
            # Access nested data
            address = user_data['address']
            print(f"  City: {address['city']}")
            print(f"  Zipcode: {address['zipcode']}")
            
        else:
            print(f"Failed to get user data: {response.status_code}")
            
    except json.JSONDecodeError:
        print("❌ Invalid JSON response")
    except KeyError as e:
        print(f"❌ Missing expected field: {e}")
    except Exception as e:
        print(f"💥 Error: {e}")


def example_multiple_requests():
    """
    Example 6: Making multiple requests efficiently
    """
    print("\n🔍 Example 6: Multiple Requests")
    print("-" * 40)
    
    # Get multiple users
    user_ids = [1, 2, 3]
    users = []
    
    for user_id in user_ids:
        try:
            response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
            
            if response.status_code == 200:
                user_data = response.json()
                users.append({
                    'id': user_data['id'],
                    'name': user_data['name'],
                    'email': user_data['email']
                })
                print(f"✅ Got user {user_id}: {user_data['name']}")
            else:
                print(f"❌ Failed to get user {user_id}")
                
        except Exception as e:
            print(f"💥 Error getting user {user_id}: {e}")
    
    print(f"\nSuccessfully retrieved {len(users)} users")


def example_real_world_api():
    """
    Example 7: Real-world API usage
    """
    print("\n🔍 Example 7: Real-world API")
    print("-" * 40)
    
    try:
        # Get a random programming joke
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        if response.status_code == 200:
            joke = response.json()
            print("Here's a programming joke for you:")
            print(f"🎭 {joke['setup']}")
            print(f"😄 {joke['punchline']}")
        else:
            print("Couldn't get a joke right now 😢")
            
    except Exception as e:
        print(f"Error getting joke: {e}")


def main():
    """
    Run all examples
    """
    print("🚀 API Request Examples")
    print("=" * 50)
    
    examples = [
        example_simple_get,
        example_get_with_parameters,
        example_custom_headers,
        example_error_handling,
        example_json_handling,
        example_multiple_requests,
        example_real_world_api
    ]
    
    for example_func in examples:
        try:
            example_func()
            time.sleep(1)  # Be nice to the APIs
        except Exception as e:
            print(f"Example failed: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 All examples completed!")
    print("Study the code above to understand how each example works.")


if __name__ == "__main__":
    main()
