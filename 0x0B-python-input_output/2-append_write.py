#!/usr/bin/python3
"""Function to append str to end of text file."""


def append_write(filename="", text=""):
    """
    Appends a str to the end of a UTF-8 encoded text file
    Returns:
    Number of charcters added to the file

    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_added = file.write(text)
    return num_added
