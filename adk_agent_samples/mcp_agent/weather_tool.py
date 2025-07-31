# ./adk_agent_samples/mcp_agent/weather_tool.py
import os
import requests
from typing import Dict, Any, Optional
from google.adk.tools.base_tool import BaseTool

class WeatherTool(BaseTool):
    """Custom weather tool that integrates with WeatherAPI.com"""
    
    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key
        self.base_url = "http://api.weatherapi.com/v1"
    
    def get_current_weather(self, location: str) -> Dict[str, Any]:
        """Get current weather for a location"""
        try:
            url = f"{self.base_url}/current.json"
            params = {
                "key": self.api_key,
                "q": location,
                "aqi": "no"
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            return {
                "location": f"{data['location']['name']}, {data['location']['region']}",
                "temperature_f": data['current']['temp_f'],
                "temperature_c": data['current']['temp_c'],
                "condition": data['current']['condition']['text'],
                "humidity": data['current']['humidity'],
                "wind_mph": data['current']['wind_mph'],
                "feels_like_f": data['current']['feelslike_f'],
                "uv_index": data['current']['uv']
            }
        except Exception as e:
            return {"error": f"Failed to get weather data: {str(e)}"}
    
    def get_forecast(self, location: str, days: int = 3) -> Dict[str, Any]:
        """Get weather forecast for a location"""
        try:
            url = f"{self.base_url}/forecast.json"
            params = {
                "key": self.api_key,
                "q": location,
                "days": min(days, 10),  # API limit is 10 days
                "aqi": "no",
                "alerts": "no"
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            forecast_days = []
            for day in data['forecast']['forecastday']:
                forecast_days.append({
                    "date": day['date'],
                    "max_temp_f": day['day']['maxtemp_f'],
                    "min_temp_f": day['day']['mintemp_f'],
                    "condition": day['day']['condition']['text'],
                    "chance_of_rain": day['day']['daily_chance_of_rain'],
                    "max_wind_mph": day['day']['maxwind_mph']
                })
            
            return {
                "location": f"{data['location']['name']}, {data['location']['region']}",
                "forecast": forecast_days
            }
        except Exception as e:
            return {"error": f"Failed to get forecast data: {str(e)}"}
    
    def get_weather_along_route(self, waypoints: list, days: int = 1) -> Dict[str, Any]:
        """Get weather for multiple locations along a route"""
        weather_data = {}
        
        for point in waypoints:
            if days == 1:
                weather_data[point] = self.get_current_weather(point)
            else:
                weather_data[point] = self.get_forecast(point, days)
        
        return weather_data