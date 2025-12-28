def is_travel_related(query: str) -> bool:  # Checks if a user query is about travel
    """
    Checks whether the user query is related to travel planning.
    """

    # Set of keywords commonly used in travel-related queries
    travel_keywords = {
        "plan", "trip", "travel", "flight", "hotel",
        "tour", "vacation", "journey", "itinerary",
        "budget", "place", "places", "visit"
    }

    # Convert query to lowercase and split it into words
    words = query.lower().split()

    # Return True if any word matches a travel keyword
    return any(word in travel_keywords for word in words)
