from langchain_core.tools import tool
from utils.data_loader import load_json

@tool
def discover_places(city: str) -> list:
    """
    Returns Top Tourist attractions for a city.

    Args:
        city (str) : Destination city

    Returns:
        list: List of attractions
    """

    places = load_json("data/places.json")

    return [p for p in places if p["city"].lower() == city.lower()]

