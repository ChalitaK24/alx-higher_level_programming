#!/usr/bin/python3
"""Function that writes an object to a text file using a JSON rep"""

import json


def save_to_json_file(my_obj, filename):
    """
    Returns an Object (Python Data structure) represented by JSON str
        my_obj (object): The python object to be serialized
        filename (str): The name of the file where the JSON str is written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
