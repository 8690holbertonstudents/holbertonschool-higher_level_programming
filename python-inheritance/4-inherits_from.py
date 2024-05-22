#!/usr/bin/python3
"""
    Module to manipulate subclasses.
"""


def inherits_from(obj, a_class):
    """
        Function that compare if the object is an instance
        of a class that inherited (directly or indirectly)
        from the specified class

        Args:
        obj: The object to compare.
        a_class: The defined class.

        Returns:
        True if exact, otherwise False.
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return (True)
    else:
        return (False)
