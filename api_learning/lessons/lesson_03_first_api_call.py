#!/usr/bin/env python3
"""
Lesson 3: Your First API Call 🚀

Learning Objectives:
- Make your first API call using Python requests
- Handle JSON responses
- Deal with errors gracefully
- Understand API keys and authentication
"""

import requests
import json

def lesson_introduction():
    """
    Introduction to making API calls with Python
    """
    print("🚀 Welcome to Lesson 3: Your First API Call")
    print("=" * 45)
    
    print("\n📖 What We'll Learn:")
    print("-" * 25)
    print("• How to use Python's 'requests' library")
    print("• Make a real API call to get data")
    print("• Handle the response")
    print("• Deal with errors")
    print("• Understand API keys")

def setup_requests():
    """
    Explain the requests library
    """
    print("\n📦 The 'requests' Library:")
    print("-" * 30)
    print("Python's most popular library for making HTTP requests")
    print()
    print("Install it with: pip install requests")
    print("Import it with: import requests")
    print()
    print("🎯 It makes API calls super easy!")

def first_api_call():
    """
    Make your very first API call
    """
    print("\n🌟 Your First API Call:")
    print("-" * 30)
    print("Let's get a random joke from a free API!")
    print()
    
    try:
        print("📡 Making request to: https://official-joke-api.appspot.com/random_joke")
        
        # Make the API call
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Success! Here's the response:")
            
            # Get JSON data
            joke_data = response.json()
            
            print(f"🎭 Setup: {joke_data['setup']}")
            print(f"😄 Punchline: {joke_data['punchline']}")
            
            print("\n🔍 Raw JSON response:")
            print(json.dumps(joke_data, indent=2))
            
        else:
            print(f"❌ Error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"💥 Network error: {e}")
    except Exception as e:
        print(f"💥 Unexpected error: {e}")

def anatomy_of_request():
    """
    Break down what happens in an API call
    """
    print("\n🔬 Anatomy of an API Call:")
    print("-" * 35)
    
    print("Here's what happens when you call requests.get():")
    print()
    print("1. 📤 Python sends HTTP request to the server")
    print("2. 🌐 Request travels over the internet")
    print("3. 🖥️  Server processes your request")
    print("4. 📥 Server sends back HTTP response")
    print("5. 🐍 Python receives and parses the response")
    print("6. 📊 You get a Response object to work with")

def response_object_explained():
    """
    Explain the response object
    """
    print("\n📋 Response Object Properties:")
    print("-" * 35)
    
    print("When you make a request, you get a Response object with:")
    print()
    
    # Make a sample request to demonstrate
    try:
        response = requests.get("https://httpbin.org/json")
        
        print(f"  📊 .status_code    → {response.status_code}")
        print(f"  📝 .text          → First 50 chars: {response.text[:50]}...")
        print(f"  🗂️  .json()        → Converts JSON to Python dict")
        print(f"  📋 .headers       → Response headers")
        print(f"  🔗 .url           → {response.url}")
        print(f"  ⏱️  .elapsed       → {response.elapsed}")
        
    except Exception as e:
        print(f"  (Demo failed: {e})")

def handling_different_responses():
    """
    Show how to handle different types of responses
    """
    print("\n🎯 Handling Different Responses:")
    print("-" * 40)
    
    print("✅ Success (200):")
    print("  if response.status_code == 200:")
    print("      data = response.json()")
    print("      # Use the data")
    print()
    
    print("❌ Not Found (404):")
    print("  if response.status_code == 404:")
    print("      print('Resource not found')")
    print()
    
    print("🔒 Unauthorized (401):")
    print("  if response.status_code == 401:")
    print("      print('Need to authenticate')")
    print()
    
    print("💥 Server Error (500):")
    print("  if response.status_code >= 500:")
    print("      print('Server is having problems')")

def api_keys_intro():
    """
    Introduce the concept of API keys
    """
    print("\n🔑 API Keys - Your Digital ID:")
    print("-" * 35)
    
    print("Many APIs require an 'API key' - think of it as your ID card")
    print()
    print("Why APIs use keys:")
    print("  🔒 Security - Know who's making requests")
    print("  📊 Tracking - Monitor usage")
    print("  💰 Billing - Charge for usage")
    print("  🚦 Rate Limiting - Prevent abuse")
    print()
    
    print("How to use API keys:")
    print("  1. Sign up for the API service")
    print("  2. Get your unique API key")
    print("  3. Include it in your requests")
    print()
    
    print("Common ways to send API keys:")
    print("  📋 Header: Authorization: Bearer your-key")
    print("  🔗 URL Parameter: ?api_key=your-key")
    print("  📝 Request Body: {'api_key': 'your-key'}")

def practical_example_with_headers():
    """
    Show a more realistic example with headers
    """
    print("\n🌟 Practical Example with Headers:")
    print("-" * 40)
    
    print("Let's make a request with custom headers:")
    print()
    
    try:
        # Example with headers
        headers = {
            'User-Agent': 'MyApp/1.0',
            'Accept': 'application/json'
        }
        
        response = requests.get(
            "https://httpbin.org/headers",
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Request successful!")
            print("📋 Headers the server saw:")
            
            for header, value in data['headers'].items():
                print(f"  {header}: {value}")
        
    except Exception as e:
        print(f"💥 Error: {e}")

def error_handling_best_practices():
    """
    Show proper error handling
    """
    print("\n🛡️ Error Handling Best Practices:")
    print("-" * 40)
    
    print("Always handle these potential errors:")
    print()
    
    example_code = '''
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raises exception for bad status codes
    data = response.json()
    return data
    
except requests.exceptions.Timeout:
    print("⏰ Request timed out")
    
except requests.exceptions.ConnectionError:
    print("🌐 Network connection error")
    
except requests.exceptions.HTTPError as e:
    print(f"📊 HTTP error: {e}")
    
except requests.exceptions.RequestException as e:
    print(f"💥 Request error: {e}")
    
except json.JSONDecodeError:
    print("📝 Invalid JSON response")
'''
    
    print(example_code)

def lesson_summary():
    """
    Summarize key points
    """
    print("\n📝 Lesson 3 Summary:")
    print("-" * 25)
    print("✅ Use requests.get() to make GET requests")
    print("✅ Check response.status_code for success/errors")
    print("✅ Use response.json() to get JSON data")
    print("✅ Always handle errors gracefully")
    print("✅ API keys are used for authentication and tracking")
    print("✅ Include headers for additional request information")
    print("✅ Use timeout to prevent hanging requests")

def hands_on_challenge():
    """
    Give students something to try
    """
    print("\n🏆 Hands-On Challenge:")
    print("-" * 30)
    print("Try these free APIs (no key required):")
    print()
    print("1. 🐱 Cat facts: https://catfact.ninja/fact")
    print("2. 🎲 Random number: https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain")
    print("3. 🌍 Country info: https://restcountries.com/v3.1/name/canada")
    print("4. 📰 Placeholder posts: https://jsonplaceholder.typicode.com/posts/1")
    print()
    print("Try making requests to these APIs and explore the responses!")

def next_steps():
    """
    Guide to next lesson
    """
    print("\n🎯 Next Steps:")
    print("-" * 15)
    print("Great! You can now make basic API calls...")
    print("Next: Working with real APIs and handling complex data")
    print()
    print("📚 Next: lesson_04_working_with_json.py")
    print("🧪 Practice: problems/problem_03_first_requests.py")

def main():
    """
    Run the complete lesson
    """
    lesson_introduction()
    setup_requests()
    first_api_call()
    anatomy_of_request()
    response_object_explained()
    handling_different_responses()
    api_keys_intro()
    practical_example_with_headers()
    error_handling_best_practices()
    lesson_summary()
    hands_on_challenge()
    next_steps()
    
    print("\n" + "=" * 45)
    print("🎉 Lesson 3 Complete! You made your first API call!")
    print("=" * 45)

if __name__ == "__main__":
    main()
