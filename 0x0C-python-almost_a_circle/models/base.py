#!/usr/bin/python3

""" Implementing Base class."""

import json


class Base:

    """ Private class atribute. """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Class constructor function.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON str representation
        """

        if list_dictionaries is None or not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON str representation
        """
        filename = f"{cls.__name__}.json"

        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:

            file.write(json_string)

    def from_json_string(json_string):
        """
        Returns the list represented by json_str
        """

        if json_string is None or json_string == "":

            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set
        """
        dummy = None

        if cls.__name__ == "Rectangle":

            dummy = cls(1, 1)

        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy
