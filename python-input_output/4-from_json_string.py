#!/usr/bin/python3
"""
    Module to use JSON.
"""
import json


def from_json_string(my_str):
    """
        Function that returns an object represented by is JSON string.

        Args:
         my_str: The JSON string of the object.

        Returns:
         The object represented from JSON string.
    """
    return (json.loads(my_str))
