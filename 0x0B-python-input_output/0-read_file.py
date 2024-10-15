#!/usr/bin/python3
    """
    Function that reads a text file.
    Functions:
        read_file: reads a text file and prints to stdout.
    """

def read_file(filename=""):
    """
    Reads a text file and prints to standard outpus.
    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

