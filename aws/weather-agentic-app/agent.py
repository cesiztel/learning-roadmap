from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import http_request
import requests
import os

from dotenv import load_dotenv

# Define a weather-focused system prompt
WEATHER_SYSTEM_PROMPT = """You are a weather assistant with HTTP capabilities. You can:

1. Make HTTP requests to the Google Weather API
2. Process and display weather forecast data
3. Provide weather information for locations all over the world

When retrieving weather information:
1. Get the API_KEY from the environment variables. You will use the API KEY for the Google APIs.
2. You can use the Google Geocoder API to retrieve the geolocation based on the city name. You can request from: 
https://maps.googleapis.com/maps/api/geocode/json?address={city_name}&key={API_KEY}
3. You can use the Google Weather API to retrieve the current conditions https://weather.googleapis.com/v1/currentConditions:lookup?key={API_KEY}&location.latitude={latitude}&location.longitude={longitude}. 

When displaying responses:
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language

Always explain the weather conditions clearly and provide context for the forecast.
"""

load_dotenv()

# @tool
# def get_api_key() -> str:
#     """Get the api key."""

#     # Implement user location lookup logic here
#     return os.getenv("API_KEY")

@tool
def get_weather(latitude: str, longitude: str) -> str:
    """Get current weather for a location."""
    api_key = os.getenv("API_KEY")  # used internally, never returned
    response = requests.get(
        "https://weather.googleapis.com/v1/currentConditions:lookup",
        params={"key": api_key, "location.latitude": latitude, "location.longitude": longitude},
    )
    return response.json()  # only weather data goes back to the model

@tool
def geocode(address: str) -> dict:
    """Convert an address into latitude/longitude."""
    api_key = os.getenv("API_KEY")  # used internally, never returned
    response = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json",
        params={"address": address, "key": api_key},
    )
    return response.json()["results"][0]["geometry"]["location"]

model = BedrockModel(
    model_id="global.anthropic.claude-sonnet-4-6",  # inference profile, not bare model ID
    region_name="eu-central-1",
)

# Create an agent with HTTP capabilities
weather_agent = Agent(
    system_prompt=WEATHER_SYSTEM_PROMPT,
    model=model,
    tools=[geocode, get_weather], # instead of get_api_key and http_request
)

# Ask the agent a question that uses the available tools
message = """
What's the current weather in Haarlem (The Netherlands)?
"""
weather_agent(message)