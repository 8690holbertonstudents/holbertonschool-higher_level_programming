#!/usr/bin/python3*
"""
    Module To use serialisation in python.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
        Function to serialize a Python dictionary to a JSON file.

        Args:
            data: A Python Dictionary with data
            filename:  The filename of the output JSON file.
                If the output file already exists it should be replaced.

        Returns:
            The output JSON file.
    """
    with open(filename, mode="w", encoding="utf-8") as My_File:
        json.dump(data, My_File)


def load_and_deserialize(filename):
    """
    Function to deserialize a JSON file and recreate Python dictionary.

    Args:
        filename: The JSON file to load.

    Returns:
        The Python dictionary.
    """
    with open(filename, mode="r", encoding="utf-8") as My_File:
        json.load(My_File)
