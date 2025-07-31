# 🚗 Road Trip Assistant Setup Instructions

## Required API Keys

### 1. Google Maps API Key
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable the **Maps JavaScript API** and **Places API**
- Create an API key
- Restrict the key to your domains for security

### 2. Weather API Key (FREE)
- Go to [WeatherAPI.com](https://www.weatherapi.com/)
- Sign up for a **free account** (1M calls/month free)
- Copy your API key from the dashboard

## Environment Variables Setup

### On macOS/Linux:
```bash
# Add to your ~/.bashrc, ~/.zshrc, or ~/.profile
export GOOGLE_MAPS_API_KEY="your_google_maps_key_here"
export WEATHER_API_KEY="your_weather_api_key_here"

# Reload your shell
source ~/.bashrc  # or ~/.zshrc
```

### On Windows (Command Prompt):
```cmd
set GOOGLE_MAPS_API_KEY=your_google_maps_key_here
set WEATHER_API_KEY=your_weather_api_key_here
```

### On Windows (PowerShell):
```powershell
$env:GOOGLE_MAPS_API_KEY="your_google_maps_key_here"
$env:WEATHER_API_KEY="your_weather_api_key_here"
```

## Project Structure
```
adk_agent_samples/
└── mcp_agent/
    ├── __init__.py
    ├── agent.py           # Main agent file
    ├── prompt.py          # Road trip prompt
    └── weather_tool.py    # Custom weather tool
```

## Installation Requirements

### Install required packages:
```bash
pip install requests google-adk-agents
```

## Testing Your Setup

### 1. Test Environment Variables:
```bash
echo $GOOGLE_MAPS_API_KEY
echo $WEATHER_API_KEY
```

### 2. Test Weather API:
```bash
curl "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=San Francisco"
```

## Running Your Agent
```bash
cd adk_agent_samples/mcp_agent
adk web
```

## 🎯 Features Your Bot Will Have:

✅ **Google Maps Integration**
- Get directions between cities
- Find places and attractions
- Calculate travel times

✅ **Real-Time Weather**
- Current weather conditions
- Multi-day forecasts
- Weather along entire route

✅ **Smart Clothing Recommendations**
- Temperature-appropriate suggestions
- Activity-based gear recommendations
- Regional climate considerations

✅ **Personalized Trip Planning**
- Budget-conscious recommendations
- Pet-friendly options
- Interest-based attractions

## 🚨 Troubleshooting

**"WARNING: API key not set"**
- Double-check environment variable names
- Restart your terminal after setting variables
- Verify with `echo $VARIABLE_NAME`

**Weather API not working**
- Verify your API key at weatherapi.com
- Check if you've exceeded free tier limits
- Ensure internet connection for API calls

**Google Maps tools not found**
- Run `npm install -g @modelcontextprotocol/server-google-maps`
- Verify Google Cloud APIs are enabled
- Check API key permissions