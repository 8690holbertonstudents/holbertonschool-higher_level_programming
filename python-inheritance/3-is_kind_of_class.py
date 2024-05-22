#!/usr/bin/python3
"""
    Module to manipulate subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
        Function that compare if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified clasd class.

        Args:
        obj: The object to compare.
        a_class: The defined class.

        Returns:
        True if exact, otherwise False.
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
