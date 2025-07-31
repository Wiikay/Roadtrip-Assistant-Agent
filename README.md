# 🚗 Road Trip Assistant Agent

> AI-powered road trip planning with Google Maps integration, real-time weather data, and smart clothing recommendations

[![Google ADK](https://img.shields.io/badge/Google-ADK-blue)](https://developers.google.com/adk)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-brightgreen)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

🗺️ **Google Maps Integration** - Get directions, find places, calculate travel times  
🌤️ **Real-Time Weather** - Current conditions and multi-day forecasts  
👔 **Smart Clothing Recommendations** - Weather-appropriate packing suggestions  
🐕 **Pet-Friendly Options** - Find pet-friendly stops and accommodations  
💰 **Budget-Conscious Planning** - Recommendations for all budget levels  
🎯 **Personalized Itineraries** - Tailored to your interests and preferences  

## 🚀 Quick Start

### 1. Get API Keys (Free!)

**Google Maps API:**
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable Maps JavaScript API and Places API
- Create and copy your API key

**Weather API (1M calls/month free):**
- Sign up at [WeatherAPI.com](https://www.weatherapi.com/)
- Copy your API key from the dashboard

### 2. Set Environment Variables

```bash
# macOS/Linux
export GOOGLE_MAPS_API_KEY="your_google_maps_key_here"
export WEATHER_API_KEY="your_weather_api_key_here"

# Windows PowerShell
$env:GOOGLE_MAPS_API_KEY="your_google_maps_key_here"
$env:WEATHER_API_KEY="your_weather_api_key_here"
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Your Assistant

```bash
cd adk_agent_samples/mcp_agent
adk web
```

## 💬 Example Conversation

```
🤖 Bot: "Hi! I'm your road trip assistant. Let's plan an amazing journey! 
        Where would you like to start your trip?"

👤 User: "San Francisco"

🤖 Bot: "Great choice! Where are you heading?"

👤 User: "Los Angeles via Big Sur"

🤖 Bot: "Perfect! How many days do you have for this trip?"

👤 User: "3 days"

🤖 Bot: "Let me learn about your preferences:
        • Traveling with pets? 🐕
        • Budget level? (Budget/Mid-range/Luxury)
        • Interests? (Nature/Food/History/Adventure)
        • Any dietary restrictions?"

[After preferences...]

🤖 Bot: "Based on your preferences, I've found an amazing route!
        
        **Day 1: SF → Monterey (2.5 hours)**
        • Stop: Half Moon Bay (dog-friendly beaches!)
        • Lunch: Sam's Chowder House (pet-friendly patio)
        
        🌤️ **Weather**: Sunny, 68°F with coastal breeze
        👔 **What to Pack**: 
        • Essentials: T-shirts, light pants
        • Layers: Light sweater for evening
        • Footwear: Walking shoes, sandals for beach
        • Accessories: Sunglasses, sun hat"
```

## 🏗️ Project Structure

```
Roadtrip-Assistant-Agent/
├── adk_agent_samples/
│   └── mcp_agent/
│       ├── __init__.py
│       ├── agent.py           # Main agent configuration
│       ├── weather_tool.py    # Custom weather integration
│       └── prompt.py          # Conversational AI prompt
├── requirements.txt           # Python dependencies
├── README.md                 # This file
└── SETUP.md                  # Detailed setup instructions
```

## 🛠️ Architecture

- **Google ADK Framework** - Core agent infrastructure
- **MCP (Model Context Protocol)** - Google Maps integration
- **WeatherAPI.com** - Real-time weather data
- **Gemini 2.0 Flash** - Conversational AI model

## 🎯 What Your Assistant Can Do

### 🗺️ Route Planning
- Multi-day itinerary creation
- Scenic route recommendations
- Travel time calculations
- Stop optimization

### 🌦️ Weather Intelligence
- Current weather at any location
- Multi-day forecasts for trip planning
- Weather along entire routes
- Climate-based clothing recommendations

### 🎨 Personalization
- Budget-conscious suggestions
- Pet-friendly accommodations
- Interest-based attractions
- Dietary restriction considerations

## 🔧 Customization

Modify `prompt.py` to:
- Change conversation style
- Add new travel preferences
- Customize response formatting
- Include additional travel categories

## 📝 API Usage

### Weather Tool Methods

```python
# Current weather
weather_tool.get_current_weather("San Francisco")

# Multi-day forecast
weather_tool.get_forecast("Big Sur", days=3)

# Weather along route
weather_tool.get_weather_along_route(["SF", "Monterey", "LA"], days=2)
```

## 🚨 Troubleshooting

**"WARNING: API key not set"**
- Check environment variable names are correct
- Restart terminal after setting variables
- Verify with: `echo $GOOGLE_MAPS_API_KEY`

**Weather API not working**
- Verify API key at weatherapi.com
- Check free tier limits (1M calls/month)
- Ensure internet connection

**Google Maps tools not found**
- Run: `npm install -g @modelcontextprotocol/server-google-maps`
- Verify Google Cloud APIs are enabled
- Check API key permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 🌟 Acknowledgments

- [Google Agent Development Kit (ADK)](https://developers.google.com/adk)
- [WeatherAPI.com](https://www.weatherapi.com/) for free weather data
- [Model Context Protocol](https://modelcontextprotocol.io/) for Google Maps integration

---

**Ready to plan your next adventure?** 🚗✨ Set up your API keys and start exploring!
