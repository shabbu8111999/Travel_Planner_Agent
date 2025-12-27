from langchain_core.tools import tool
from utils.data_loader import load_json


@tool
def recommend_hotel(city: str) -> dict:
    """
    Recommends the Best Rated Hotel within Budget.

    Args:
        city (str) : Destination city

    Returns:
        dict: Hotel details
    """

    hotels = load_json("data/hotels.json")

    filtered = [h for h in hotels if h["city"].lower() == city.lower()]
    if not filtered:
        return {}
    
    return max(filtered, key = lambda x: x["rating"])


