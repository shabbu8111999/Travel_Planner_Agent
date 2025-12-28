# Import json module to work with JSON data
import json

# Defines a function to load and return JSON data from a file
def load_json(file_path: str) -> list:
    """
    Loads a JSON File and return its content as Python List.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: Parsed JSON Data.
    """

    # Open the JSON file in read mode with UTF-8 encoding
    with open(file_path, "r", encoding="utf-8") as file:
        
        # Convert JSON content into Python data structure and return it
        return json.load(file)