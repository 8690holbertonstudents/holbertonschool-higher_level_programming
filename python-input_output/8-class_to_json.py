#!/usr/bin/python3
"""
    Module to use JSON.
"""
import json


def class_to_json(obj):
    """
        Function that returns the dictionary description
        with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object.

        Args:
         obj: An instance of a Class.

        Returns:
         the dictionary description.
    """
    return(obj.__dict__)
