#!/bin/usr/python3
"""Function Initializes the Student with first name, last name, and age"""


class Student:
    """Class that defines a student wiht first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        """
        first_name (str): The student's first name.
        last_name (str): The student's last name
        age (int): The strudent's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Function retrives dictionary rep of Student
        Returns:
            dict: dictionary containing the the student's attributes
        """

        return self.__dict__
