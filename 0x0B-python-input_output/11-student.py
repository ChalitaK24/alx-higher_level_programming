#!/usr/bin/python3
""" Class that defines a student with first name, last name and age."""


class Student:
    """
    first_name (str): The first name of the student.
    last_name (str): The last name of the student.
    age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Function initializes Student with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, a=None):
        """
        Function to retrive dictionary representation of Student
        a (list): A list of attribute names to retrieve (optional).
         Returns:
            dict: A dictionary containing the specified attr, or all attr.
        """
        if a is None:
            return self.__dict__
        elif isinstance(a, list) and all(isinstance(attr, str) for attr in a):
            return {attr: getattr(self, attr) for attr in a
                    if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Function replaces all atr of Student with those from the json dict
        json (dict): A dictionary containing new values for the attributes.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
