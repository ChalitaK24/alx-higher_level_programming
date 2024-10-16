#!/usr/bin/python3
"""Function that returns the dicttionary desc with simple data struct"""


def class_to_json(obj):
    """
     obj: An instance of a class
      Returns:
        A dictionary containing all serializable attributes
    """

    return obj.__dict__
