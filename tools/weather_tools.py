import requests
from langchain_core.tools import tool


@tool
def get_weather(latitude: float, longitude: float) -> dict:
    """
    Fetches the Weather Forecast using Open-Meteo API.

    Args:
        latitude (float)
        longitude (float)

    Returns:
        dict: Weather Forecast details
    """

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=temperature_2m_max&timezone=auto"
    )

    response = requests.get(url)
    return response.json()

