#!/usr/bin/python3
"""
    Module to define f the object
    is exactly an instance of the specified class.

    Args:
    obj: The object to compare.
    a_class: The defined class.
"""


def is_same_class(obj, a_class):

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
