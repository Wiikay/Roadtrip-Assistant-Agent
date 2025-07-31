#!/usr/bin/env python3
"""
Test script for Road Trip Assistant Weather Integration
Run this in codespace to verify weather functionality works
"""

import sys
import os
import json

# Add project path
sys.path.append('adk_agent_samples/mcp_agent')

def test_weather_tool():
    """Test the weather tool functionality"""
    print("🌤️ TESTING WEATHER TOOL")
    print("=" * 50)
    
    # Check if weather API key is set
    weather_api_key = os.environ.get("WEATHER_API_KEY")
    if not weather_api_key or weather_api_key == "your_weather_api_key_here":
        print("❌ WEATHER_API_KEY not set!")
        print("Set it with: export WEATHER_API_KEY='your_actual_key'")
        return False
    
    try:
        from weather_tool import WeatherTool
        weather_tool = WeatherTool(weather_api_key)
        print("✅ Weather tool imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import weather tool: {e}")
        return False
    
    # Test 1: Current Weather
    print("\n📍 Test 1: Current Weather for San Francisco")
    try:
        result = weather_tool.get_current_weather("San Francisco")
        if "error" in result:
            print(f"❌ Weather API Error: {result['error']}")
            return False
        else:
            print("✅ Current weather retrieved successfully!")
            print(f"   Location: {result.get('location', 'N/A')}")
            print(f"   Temperature: {result.get('temperature_f', 'N/A')}°F")
            print(f"   Condition: {result.get('condition', 'N/A')}")
            print(f"   Humidity: {result.get('humidity', 'N/A')}%")
    except Exception as e:
        print(f"❌ Current weather test failed: {e}")
        return False
    
    # Test 2: Weather Forecast
    print("\n📅 Test 2: 3-day Forecast for Los Angeles")
    try:
        forecast = weather_tool.get_forecast("Los Angeles", 3)
        if "error" in forecast:
            print(f"❌ Forecast API Error: {forecast['error']}")
            return False
        else:
            print("✅ Weather forecast retrieved successfully!")
            print(f"   Location: {forecast.get('location', 'N/A')}")
            for i, day in enumerate(forecast.get('forecast', [])[:2]):  # Show first 2 days
                print(f"   Day {i+1}: {day.get('date')} - {day.get('condition')}")
                print(f"          High: {day.get('max_temp_f')}°F, Low: {day.get('min_temp_f')}°F")
    except Exception as e:
        print(f"❌ Forecast test failed: {e}")
        return False
    
    # Test 3: Route Weather
    print("\n🗺️ Test 3: Weather Along Route (SF → LA)")
    try:
        route_weather = weather_tool.get_weather_along_route(
            ["San Francisco", "Monterey", "Los Angeles"], 1
        )
        print("✅ Route weather retrieved successfully!")
        for location, weather_data in route_weather.items():
            if "error" not in weather_data:
                temp = weather_data.get('temperature_f', 'N/A')
                condition = weather_data.get('condition', 'N/A')
                print(f"   📍 {location}: {temp}°F, {condition}")
            else:
                print(f"   ❌ {location}: {weather_data['error']}")
    except Exception as e:
        print(f"❌ Route weather test failed: {e}")
        return False
    
    print("\n🎉 All weather tests passed!")
    return True

def test_agent_import():
    """Test if agent can be imported (requires ADK)"""
    print("\n🤖 TESTING AGENT IMPORT")
    print("=" * 50)
    
    try:
        from agent import root_agent
        print("✅ Agent imported successfully!")
        print(f"   Agent name: {root_agent.name}")
        print(f"   Agent model: {root_agent.model}")
        print(f"   Number of tools: {len(root_agent.tools)}")
        return True
    except ImportError as e:
        print(f"⚠️ Agent import failed: {e}")
        print("   This is expected if Google ADK isn't available in codespace")
        return False
    except Exception as e:
        print(f"❌ Agent import error: {e}")
        return False

def test_prompt_import():
    """Test if prompt can be imported"""
    print("\n💬 TESTING PROMPT IMPORT")
    print("=" * 50)
    
    try:
        from prompt import instruction
        print("✅ Prompt imported successfully!")
        print(f"   Prompt length: {len(instruction)} characters")
        print("   First 150 characters:")
        print(f"   {instruction[:150]}...")
        return True
    except ImportError as e:
        print(f"❌ Prompt import failed: {e}")
        return False

def simulate_conversation():
    """Simulate a conversation with the assistant"""
    print("\n🎭 SIMULATING CONVERSATION")
    print("=" * 50)
    
    weather_api_key = os.environ.get("WEATHER_API_KEY")
    if not weather_api_key or weather_api_key == "your_weather_api_key_here":
        print("❌ Cannot simulate conversation without WEATHER_API_KEY")
        return
    
    try:
        from weather_tool import WeatherTool
        weather_tool = WeatherTool(weather_api_key)
        
        print("🤖 Bot: Hi! I'm your road trip assistant. Let's plan an amazing journey! 🚗")
        print("       Where would you like to start your trip?")
        
        # Simulate user input
        start_location = "San Francisco"
        print(f"👤 User: {start_location}")
        
        # Get weather for start location
        weather = weather_tool.get_current_weather(start_location)
        if "error" not in weather:
            temp = weather.get('temperature_f', 'N/A')
            condition = weather.get('condition', 'N/A')
            print(f"🤖 Bot: Great choice! Current weather in {start_location}:")
            print(f"       🌤️ {temp}°F and {condition.lower()}")
            print("       Where are you heading?")
            
            # Simulate destination
            destination = "Los Angeles via Big Sur"
            print(f"👤 User: {destination}")
            
            print(f"🤖 Bot: Perfect! Let me check the weather along your route...")
            
            # Get route weather
            route_weather = weather_tool.get_weather_along_route(
                ["San Francisco", "Big Sur", "Los Angeles"], 1
            )
            
            print("       Here's what to expect:")
            for location, weather_data in route_weather.items():
                if "error" not in weather_data:
                    temp = weather_data.get('temperature_f', 'N/A')
                    condition = weather_data.get('condition', 'N/A')
                    print(f"       📍 {location}: {temp}°F, {condition}")
            
            print("\n       👔 **Packing Recommendations:**")
            print("       • Layers for temperature changes")
            print("       • Light jacket for coastal areas")
            print("       • Comfortable walking shoes")
            print("       • Sunglasses and sunscreen")
            
        else:
            print(f"🤖 Bot: Sorry, I couldn't get weather data: {weather['error']}")
            
    except Exception as e:
        print(f"❌ Conversation simulation failed: {e}")

def main():
    """Run all tests"""
    print("🚀 ROAD TRIP ASSISTANT - CODESPACE TESTING")
    print("=" * 60)
    
    # Check environment
    print("\n🔧 ENVIRONMENT CHECK")
    print("=" * 30)
    google_key = os.environ.get("GOOGLE_MAPS_API_KEY", "Not set")
    weather_key = os.environ.get("WEATHER_API_KEY", "Not set")
    print(f"Google Maps API Key: {'✅ Set' if google_key != 'Not set' else '❌ Not set'}")
    print(f"Weather API Key: {'✅ Set' if weather_key != 'Not set' else '❌ Not set'}")
    
    # Run tests
    weather_success = test_weather_tool()
    agent_success = test_agent_import() 
    prompt_success = test_prompt_import()
    
    if weather_success:
        simulate_conversation()
    
    # Summary
    print("\n📊 TEST SUMMARY")
    print("=" * 30)
    print(f"Weather Tool: {'✅ PASS' if weather_success else '❌ FAIL'}")
    print(f"Agent Import: {'✅ PASS' if agent_success else '⚠️ SKIP'}")
    print(f"Prompt Import: {'✅ PASS' if prompt_success else '❌ FAIL'}")
    
    if weather_success and prompt_success:
        print("\n🎉 Core functionality is working!")
        print("Your road trip assistant is ready for testing!")
    else:
        print("\n⚠️ Some components need attention.")
        print("Check the error messages above for guidance.")

if __name__ == "__main__":
    main()