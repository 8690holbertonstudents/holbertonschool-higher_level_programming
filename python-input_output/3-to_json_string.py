#!/usr/bin/python3
"""
    Module to use JSON.
"""
import json


def to_json_string(my_obj):
    """
        Function that returns the JSON representation of an object (string).

        Args:
         my_obj: The object to describe with JSON.

        Returns:
         my_obj representation string.
    """
    return (json.dumps(my_obj))
