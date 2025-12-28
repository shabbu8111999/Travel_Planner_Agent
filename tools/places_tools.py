# Import tool decorator to expose function as a LangChain tool
from langchain_core.tools import tool

# Import utility function to load place data from JSON file
from utils.data_loader import load_json


@tool  # Marks this function as an LLM-callable tool
def discover_places(city: str) -> list:
    """
    Returns top tourist attractions for a given city.

    Args:
        city (str): Destination city name

    Returns:
        list: List of tourist attractions
    """

    # Load places data from JSON file
    places = load_json("data/places.json")

    # Filter and return places matching the given city
    return [p for p in places if p["city"].lower() == city.lower()]
