#!/usr/bin/python3
"""
    Module to manipulate object.
"""


def lookup(obj):
    """
        function that returns the list of available
        attributes and methods of an object:
    """
    return (list(dir(obj)))
