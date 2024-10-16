#!/usr/bin/python3

def class_to_json(obj):
    """
     Function that returns the dict desc with simple data struc
     obj: An instance of a class.
      Returns:
        A dictionary containing all serializable attributes
    """

    return obj.__dict__
