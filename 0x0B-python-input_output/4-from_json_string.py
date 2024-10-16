#!/usr/bin/python3
"""Function that returns an obj rep  by a JSON string."""

import json
"""
Returns an object rep by a JSON string

"""


def from_json_string(my_str):
    """
    Args:
        my_str (str): The JSON string to be deserialized.
    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
