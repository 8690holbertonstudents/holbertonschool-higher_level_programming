#!/usr/bin/python3
"""
    Module to manipulate subclasses.
"""


def is_same_class(obj, a_class):
    """
        Function that compare if the object
        is exactly an instance of the specified class.

        Args:
        obj: The object to compare.
        a_class: The defined class.

        Returns:
        True if exact, otherwise False.
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
