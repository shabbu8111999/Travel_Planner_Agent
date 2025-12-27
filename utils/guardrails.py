def is_travel_related(query: str) -> bool:
    """
    Checks whether the user query is related to travel planning.
    """
    travel_keywords = {
        "plan", "trip", "travel", "flight", "hotel",
        "tour", "vacation", "journey", "itinerary",
        "budget", "place", "places", "visit"
    }

    words = query.lower().split()
    return any(word in travel_keywords for word in words)
