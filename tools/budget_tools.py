from langchain_core.tools import tool


@tool
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
    return flight + (hotel * days) + food_travel

