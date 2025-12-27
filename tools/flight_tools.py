
from langchain_core.tools import tool
from utils.data_loader import load_json


@tool
def search_flight(source: str, destination: str) -> dict:
    """
    Finds the cheapest flight between source and destination.

    Args:
        source (str) : Departure City
        destination (str) : Arrival City

    Returns:
        dict: Selected flights details
    """

    flights = load_json("data/flights.json")


    available = [
        f for f in flights
        if f["source"].lower() == source.lower()
        and f["destination"].lower() == destination.lower()
    ]

    if not available:
        return {}
    
    return min(available, key = lambda x: x["price"])

