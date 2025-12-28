# Helper utilities for language handling

def build_prompt(user_query: str, language: str) -> str:  # Builds a multilingual-friendly prompt for the agent
    """
    Prepares the user query for multilingual support.

    If the selected language is not English:
    - Translate the query to English internally
    - Plan the trip in English
    - Translate the final response back to the selected language

    Args:
        user_query (str): Original user input
        language (str): Preferred communication language

    Returns:
        str: Prompt sent to the agent
    """

    # If language is English, return the query as-is
    if language == "English":
        return user_query

    # Create instructions for internal translation and response generation
    return (
        f"You are given a travel-related user query written in {language}.\n\n"
        f"INSTRUCTIONS:\n"
        f"1. Translate the query into English.\n"
        f"2. Plan the complete trip in English.\n"
        f"3. Translate the FINAL answer back into {language}.\n"
        f"4. Do not mention that translation was done.\n\n"
        f"USER QUERY:\n"
        f"{user_query}"
    )