#!/usr/bin/python3
""" A class that defines a student with first name, last name, and age."""


class Student:
    """
     first_name (str): The first name of the student.
     last_name (str): The last name of the student.
     age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Function initializes Student with first name, last name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, a=None):
        """
        function retrives a dictionary representation of the Student instance.
        attrs (list): A list of attribute names to retrieve (optional).
        Returns:
            dict: A dict containing the specified attr or all attr
        """
        if a is None:
            return self.__dict__
        elif isinstance(a, list) and all(isinstance(atr, str) for atr in a):
            return {atr: getattr(self, atr) for atr in a if hasattr(self, atr)}
        else:
            return self.__dict__
