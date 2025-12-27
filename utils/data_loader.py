import json


def load_json(file_path: str) -> list:
    """
    Loads a JSON File and return its content as Python List.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: Parsed JSON Data.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)