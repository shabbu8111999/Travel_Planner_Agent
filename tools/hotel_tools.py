# Import tool decorator to expose function as a LangChain tool
from langchain_core.tools import tool

# Import utility function to load hotel data from JSON file
from utils.data_loader import load_json


@tool  # Marks this function as an LLM-callable tool
def recommend_hotel(city: str) -> dict:
    """
    Recommends the Best Rated Hotel within Budget.

    Args:
        city (str) : Destination city

    Returns:
        dict: Hotel details
    """

    # Load hotel data from JSON file
    hotels = load_json("data/hotels.json")

    # Filter hotels that match the given city 
    filtered = [h for h in hotels if h["city"].lower() == city.lower()]
    
    # Return empty dict if no hotels are found
    if not filtered:
        return {}
    
    # Select and return the hotel with the highest rating
    return max(filtered, key = lambda x: x["rating"])


