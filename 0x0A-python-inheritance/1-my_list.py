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
        sorted_list = sorted(self)

        print(sorted_list)
