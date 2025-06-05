#!/usr/bin/env python3
"""
Lesson 2: HTTP Basics 🌐

Learning Objectives:
- Understand what HTTP is
- Learn about HTTP methods (GET, POST, PUT, DELETE)
- Understand status codes
- Learn about headers and request/response structure
"""

def lesson_introduction():
    """
    Introduction to HTTP - the foundation of web APIs
    """
    print("🌐 Welcome to Lesson 2: HTTP Basics")
    print("=" * 40)
    
    print("\n📖 What is HTTP?")
    print("-" * 20)
    print("HTTP = HyperText Transfer Protocol")
    print("It's the 'language' that web browsers and servers use to talk")
    print()
    print("Think of it as the 'rules of conversation' between:")
    print("  📱 Client (your app, browser)")
    print("  🖥️  Server (website, API)")

def http_methods():
    """
    Explain the main HTTP methods
    """
    print("\n🔧 HTTP Methods (Verbs):")
    print("-" * 30)
    print("Just like in English, we have different 'action words':")
    print()
    
    methods = [
        ("GET", "📖 Read/Retrieve data", "Get me the weather"),
        ("POST", "➕ Create new data", "Create a new user account"),
        ("PUT", "✏️  Update existing data", "Update my profile"),
        ("DELETE", "🗑️  Remove data", "Delete my post"),
        ("PATCH", "🔧 Partially update", "Change just my email")
    ]
    
    for method, description, example in methods:
        print(f"  {method:6} - {description}")
        print(f"         Example: '{example}'")
        print()

def status_codes():
    """
    Explain HTTP status codes
    """
    print("\n📊 HTTP Status Codes:")
    print("-" * 25)
    print("The server's way of saying 'here's what happened':")
    print()
    
    codes = [
        ("2xx", "✅ Success", "200 OK - Everything worked!"),
        ("3xx", "↩️  Redirect", "301 Moved - Content moved somewhere else"),
        ("4xx", "❌ Client Error", "404 Not Found - You asked for something that doesn't exist"),
        ("5xx", "💥 Server Error", "500 Internal Error - Server broke")
    ]
    
    for code_range, meaning, example in codes:
        print(f"  {code_range} - {meaning}")
        print(f"       {example}")
        print()
    
    print("🎯 Common ones you'll see:")
    common_codes = [
        "200 - OK (success)",
        "201 - Created (new resource made)",
        "400 - Bad Request (you sent wrong data)",
        "401 - Unauthorized (need to login)",
        "404 - Not Found (doesn't exist)",
        "500 - Server Error (server problem)"
    ]
    
    for code in common_codes:
        print(f"    • {code}")

def request_response_structure():
    """
    Show what HTTP requests and responses look like
    """
    print("\n📡 Request & Response Structure:")
    print("-" * 35)
    
    print("📤 HTTP Request has:")
    print("  1. Method (GET, POST, etc.)")
    print("  2. URL (where to send it)")
    print("  3. Headers (extra info)")
    print("  4. Body (data, if needed)")
    print()
    
    print("Example Request:")
    print("  GET /weather?city=London HTTP/1.1")
    print("  Host: api.weather.com")
    print("  Authorization: Bearer your-api-key")
    print()
    
    print("📥 HTTP Response has:")
    print("  1. Status Code (200, 404, etc.)")
    print("  2. Headers (info about response)")
    print("  3. Body (the actual data)")
    print()
    
    print("Example Response:")
    print("  HTTP/1.1 200 OK")
    print("  Content-Type: application/json")
    print("  ")
    print("  {")
    print('    "city": "London",')
    print('    "temperature": "15°C"')
    print("  }")

def headers_explained():
    """
    Explain what headers are and common ones
    """
    print("\n📋 Headers Explained:")
    print("-" * 25)
    print("Headers are like 'metadata' - extra info about the request/response")
    print()
    
    common_headers = [
        ("Content-Type", "What kind of data is this?", "application/json"),
        ("Authorization", "Who are you?", "Bearer abc123"),
        ("User-Agent", "What app/browser?", "MyApp/1.0"),
        ("Accept", "What data types can you handle?", "application/json"),
        ("Cache-Control", "How long to store this?", "max-age=3600")
    ]
    
    for header, purpose, example in common_headers:
        print(f"  {header}:")
        print(f"    Purpose: {purpose}")
        print(f"    Example: {example}")
        print()

def url_structure():
    """
    Break down URL components
    """
    print("\n🔗 URL Structure:")
    print("-" * 20)
    print("Let's break down a URL:")
    print()
    print("https://api.weather.com/v1/weather?city=London&units=metric")
    print("│     │              │  │       │                    │")
    print("│     │              │  │       │                    └─ Parameters")
    print("│     │              │  │       └─ Endpoint")
    print("│     │              │  └─ Version")
    print("│     │              └─ Path")
    print("│     └─ Domain")
    print("└─ Protocol")
    print()
    
    print("🎯 Parts explained:")
    parts = [
        ("Protocol", "https://", "How to connect (secure)"),
        ("Domain", "api.weather.com", "Which server"),
        ("Path", "/v1/weather", "What resource"),
        ("Parameters", "?city=London", "Extra details")
    ]
    
    for part, example, explanation in parts:
        print(f"  {part}: {example} - {explanation}")

def practical_example():
    """
    Show a real-world example
    """
    print("\n🌟 Practical Example:")
    print("-" * 25)
    print("Let's say you want to get user info from a social media API:")
    print()
    
    print("📤 Request:")
    print("  Method: GET")
    print("  URL: https://api.social.com/users/123")
    print("  Headers:")
    print("    Authorization: Bearer your-token")
    print("    Accept: application/json")
    print()
    
    print("📥 Response:")
    print("  Status: 200 OK")
    print("  Headers:")
    print("    Content-Type: application/json")
    print("  Body:")
    print("    {")
    print('      "id": 123,')
    print('      "name": "John Doe",')
    print('      "email": "john@example.com"')
    print("    }")

def lesson_summary():
    """
    Summarize key points
    """
    print("\n📝 Lesson 2 Summary:")
    print("-" * 25)
    print("✅ HTTP is the protocol for web communication")
    print("✅ Main methods: GET (read), POST (create), PUT (update), DELETE (remove)")
    print("✅ Status codes tell you what happened (200=success, 404=not found, etc.)")
    print("✅ Requests have method, URL, headers, and optional body")
    print("✅ Responses have status, headers, and body")
    print("✅ Headers provide extra information about requests/responses")

def next_steps():
    """
    Guide to next lesson
    """
    print("\n🎯 Next Steps:")
    print("-" * 15)
    print("Now you understand HOW APIs communicate...")
    print("Next: Let's make your first API call with Python!")
    print()
    print("📚 Next: lesson_03_first_api_call.py")
    print("🧪 Practice: problems/problem_02_http_concepts.py")

def main():
    """
    Run the complete lesson
    """
    lesson_introduction()
    http_methods()
    status_codes()
    request_response_structure()
    headers_explained()
    url_structure()
    practical_example()
    lesson_summary()
    next_steps()
    
    print("\n" + "=" * 40)
    print("🎉 Lesson 2 Complete! You understand HTTP basics!")
    print("=" * 40)

if __name__ == "__main__":
    main()
