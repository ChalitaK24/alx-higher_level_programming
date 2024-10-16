#!/usr/bin/python3
"""
Function to wrte a text file and return character num.

"""


def write_file(filename="", text=""):
    """
    Write str to a UTF-8 encoded txt file and returns numberof char

    Returns:
    The number of charcters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        no_char = file.write(text)
    return no_char
