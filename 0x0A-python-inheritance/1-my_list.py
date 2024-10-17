#!/usr/bin/python3

"""A class that inherits from the list"""

class MyList(list):

    def print_sorted(self):
        """
        Function prints the sorted list in ascending order
        """
        print(sorted(self))
