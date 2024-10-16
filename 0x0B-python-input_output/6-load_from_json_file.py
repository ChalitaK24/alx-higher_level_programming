#!/usr/bin/python3
"""Creates an Object (Python data structure) from a JSON file """
import json


def load_from_json_file(filename):
    """
    filename (str): The name of the file containing the JSON str.
    Returns:
        Object: The Python object represented by the JSON str in the file.

    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
