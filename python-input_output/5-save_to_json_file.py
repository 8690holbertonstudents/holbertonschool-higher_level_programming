#!/usr/bin/python3
"""
    Module to use JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Function that writes an Object to a text file,
        using a JSON representation.

        Args:
         my_obj: The object to represent in JSON string.
         filename: The text file to write in.

        Returns:
         Write the object JSON string to a text file.
    """
    with open(filename, mode="w", encoding="utf-8") as My_File:
        read_data = My_File.write(json.dumps(my_obj, sort_keys=True))
