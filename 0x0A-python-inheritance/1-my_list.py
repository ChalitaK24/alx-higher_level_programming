#!/usr/bin/python3

"""A class that inherits from the list"""


class MyList(list):
    """
    Subclass of the built-in list class to be printed in ascending order
    """
    def print_sorted(self):
        """
        Function prints the sorted list in ascending order
        """
        print(sorted(self))

    def __repr__(self):
        """
        Returns MyList instance in the format MyList([...])
        """
        return f"MyList({super().__repr__()})"
