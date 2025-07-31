# ./adk_agent_samples/mcp_agent/agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from .weather_tool import WeatherTool
from . import prompt

# Retrieve API keys from environment variables
google_maps_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
weather_api_key = os.environ.get("WEATHER_API_KEY")  # New weather API key

# Google Maps API key check
if not google_maps_api_key:
    google_maps_api_key = "YOUR_GOOGLE_MAPS_API_KEY_HERE"
    if google_maps_api_key == "YOUR_GOOGLE_MAPS_API_KEY_HERE":
        print("WARNING: GOOGLE_MAPS_API_KEY is not set. Please set it as an environment variable.")
        print("Example: export GOOGLE_MAPS_API_KEY='your_actual_key_here'")

# Weather API key check  
if not weather_api_key:
    weather_api_key = "YOUR_WEATHER_API_KEY_HERE"
    if weather_api_key == "YOUR_WEATHER_API_KEY_HERE":
        print("WARNING: WEATHER_API_KEY is not set. Please set it as an environment variable.")
        print("Get a free API key from: https://www.weatherapi.com/")
        print("Example: export WEATHER_API_KEY='your_actual_key_here'")

# Initialize weather tool
weather_tool = WeatherTool(weather_api_key) if weather_api_key != "YOUR_WEATHER_API_KEY_HERE" else None

# Build tools list
tools = [
    # Google Maps MCP Toolset
    MCPToolset(
        connection_params=StdioServerParameters(
            command='npx',
            args=[
                "-y",
                "@modelcontextprotocol/server-google-maps",
            ],
            env={
                "GOOGLE_MAPS_API_KEY": google_maps_api_key
            }
        ),
    )
]

# Add weather tool if API key is available
if weather_tool:
    tools.append(weather_tool)

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='roadtrip_assistant_agent',
    instruction=prompt.instruction,
    tools=tools,
)