#!/usr/bin/python3
"""
    Module to use JSON.
"""
import json


def load_from_json_file(filename):
    """
        Function that creates an Object from a “JSON file”.

        Args:
         filename: The JSON file to read.

        Returns:
         Object created from JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as My_File:
        return (json.load(My_File))
