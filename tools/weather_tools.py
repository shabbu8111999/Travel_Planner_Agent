# Import requests library to make HTTP API calls
import requests

# Import tool decorator to expose function as a LangChain tool
from langchain_core.tools import tool


@tool  # Marks this function as an LLM-callable tool
def get_weather(latitude: float, longitude: float) -> dict:
    """
    Fetches the weather forecast using Open-Meteo API.

    Args:
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location

    Returns:
        dict: Weather forecast details
    """

    # Construct the Open-Meteo API URL with query parameters
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=temperature_2m_max&timezone=auto"
    )

    # Send GET request to the weather API
    response = requests.get(url)

    # Convert API response to JSON and return it
    return response.json()
