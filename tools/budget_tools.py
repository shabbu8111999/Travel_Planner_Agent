# Import tool decorator to register a function as a LangChain tool
from langchain_core.tools import tool


@tool  # Marks this function as a usable tool for an LLM/agent
def estimate_budget(flight: int, hotel: int, days: int) -> int:
    """
    Estimates total travel budget.

    Args:
        flight (int) : Flight cost
        hotel (int) : Per night hotel cost
        days (int) : Number of days

    Returns:
        int: Total estimated budget
    """

    food_travel = days * 800 # Assuming a fixed daily cost for food and local travel
    
    # Returns the total budget (flight + hotel stay + food & travel)
    return flight + (hotel * days) + food_travel

