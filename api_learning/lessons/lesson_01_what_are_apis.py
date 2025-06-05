#!/usr/bin/env python3
"""
Lesson 1: What Are APIs? 🤔

Learning Objectives:
- Understand what an API is in simple terms
- Learn why APIs are important
- See real-world examples of APIs
- Understand the client-server model
"""

def lesson_introduction():
    """
    Welcome to API Learning! Let's start with the absolute basics.
    """
    print("🚀 Welcome to Lesson 1: What Are APIs?")
    print("=" * 50)
    
    print("\n📖 What is an API?")
    print("-" * 20)
    print("API stands for 'Application Programming Interface'")
    print("Think of it as a waiter in a restaurant:")
    print("  👤 You (client) want food")
    print("  🍽️  Kitchen (server) can make food") 
    print("  👨‍🍳 Waiter (API) takes your order and brings food back")
    print("\nThe API is the messenger that:")
    print("  • Takes your request")
    print("  • Tells the system what you want")
    print("  • Brings back the response")

def real_world_examples():
    """
    Show concrete examples of APIs we use every day
    """
    print("\n🌍 APIs You Use Every Day:")
    print("-" * 30)
    
    examples = [
        ("Weather App", "Gets weather data from weather service"),
        ("Social Media", "Posts your photos, gets friend updates"),
        ("Maps App", "Gets directions and traffic data"),
        ("Online Shopping", "Checks prices, processes payments"),
        ("Music Streaming", "Gets song data, creates playlists"),
        ("Banking App", "Checks balance, transfers money")
    ]
    
    for app, description in examples:
        print(f"  📱 {app}: {description}")

def api_analogy():
    """
    Use a simple analogy to explain APIs
    """
    print("\n🏪 The Restaurant Analogy:")
    print("-" * 30)
    print("Imagine you're at a restaurant:")
    print("  1. 👤 You (Client) look at the menu")
    print("  2. 📋 Menu (API Documentation) shows what's available")
    print("  3. 🗣️  You tell waiter (API) your order")
    print("  4. 👨‍🍳 Kitchen (Server) prepares your food")
    print("  5. 🍽️  Waiter (API) brings your food back")
    print("  6. 😋 You enjoy your meal (Use the data)")
    
    print("\nIn programming terms:")
    print("  • Menu = API Documentation")
    print("  • Order = HTTP Request")
    print("  • Food = Data/Response")
    print("  • Waiter = API")

def types_of_apis():
    """
    Explain different types of APIs
    """
    print("\n🔧 Types of APIs:")
    print("-" * 20)
    
    api_types = [
        ("REST API", "Most common, uses HTTP methods (GET, POST, etc.)"),
        ("GraphQL", "Query exactly the data you need"),
        ("SOAP", "Older, more formal protocol"),
        ("WebSocket", "Real-time, two-way communication")
    ]
    
    for api_type, description in api_types:
        print(f"  🔹 {api_type}: {description}")
    
    print("\n💡 We'll focus on REST APIs - they're the most popular!")

def why_apis_matter():
    """
    Explain the importance of APIs
    """
    print("\n⭐ Why APIs Are Important:")
    print("-" * 30)
    
    benefits = [
        "🔗 Connect different applications",
        "♻️  Reuse existing functionality", 
        "⚡ Build faster (don't reinvent the wheel)",
        "🌐 Access data from anywhere",
        "🔧 Separate frontend and backend",
        "📈 Scale applications efficiently"
    ]
    
    for benefit in benefits:
        print(f"  {benefit}")

def simple_api_example():
    """
    Show what an API request looks like conceptually
    """
    print("\n📡 Simple API Example:")
    print("-" * 25)
    print("Let's say you want to get weather for London:")
    print()
    print("  📤 Your Request:")
    print("     'Hey weather API, give me London's weather'")
    print()
    print("  📥 API Response:")
    print("     {")
    print('       "city": "London",')
    print('       "temperature": "15°C",')
    print('       "condition": "Cloudy"')
    print("     }")
    print()
    print("  🎯 You get exactly what you asked for!")

def lesson_summary():
    """
    Summarize key points from this lesson
    """
    print("\n📝 Lesson 1 Summary:")
    print("-" * 25)
    print("✅ API = Application Programming Interface")
    print("✅ APIs are like waiters - they take requests and bring responses")
    print("✅ We use APIs every day (weather, social media, maps, etc.)")
    print("✅ APIs help applications talk to each other")
    print("✅ REST APIs are the most common type")
    print("✅ APIs make development faster and more efficient")

def next_steps():
    """
    Guide to the next lesson
    """
    print("\n🎯 Next Steps:")
    print("-" * 15)
    print("Now that you understand WHAT APIs are...")
    print("Next lesson: HOW they work (HTTP basics)")
    print()
    print("📚 Next: lesson_02_http_basics.py")
    print("🧪 Practice: problems/problem_01_api_concepts.py")

def main():
    """
    Run the complete lesson
    """
    lesson_introduction()
    real_world_examples()
    api_analogy()
    types_of_apis()
    why_apis_matter()
    simple_api_example()
    lesson_summary()
    next_steps()
    
    print("\n" + "=" * 50)
    print("🎉 Lesson 1 Complete! You now understand what APIs are!")
    print("=" * 50)

if __name__ == "__main__":
    main()
