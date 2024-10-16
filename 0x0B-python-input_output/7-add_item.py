#!/usr/bin/python3
"""Adds all command-line arguments to a list and saves them to a JSON file."""

import sys

from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'


def add_items_to_json():
    """
    Function adds all command line arguments to a list on a JSON file
    Returns:
        None
    """


if exists(filename):

    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
