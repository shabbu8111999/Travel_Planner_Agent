# Import tool decorator to expose function as a LangChain tool
from langchain_core.tools import tool

# Import helper function to load JSON data from file
from utils.data_loader import load_json


@tool  # Marks this function as an LLM-callable tool
def search_flight(source: str, destination: str) -> dict:
    """
    Finds the cheapest flight between source and destination.

    Args:
        source (str) : Departure City
        destination (str) : Arrival City

    Returns:
        dict: Selected flights details
    """

    # Loads flight data from JSON file
    flights = load_json("data/flights.json")

    # Filter flights matching source and destination
    available = [
        f for f in flights
        if f["source"].lower() == source.lower()
        and f["destination"].lower() == destination.lower()
    ]

    # Return empty dict if no flights are found
    if not available:
        return {}
    
    # Select and return the flight with the lowest price
    return min(available, key = lambda x: x["price"])

