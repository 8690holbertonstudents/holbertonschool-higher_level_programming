#!/usr/bin/python3
"""
    Python script for using doctest.
    Using a .txt file in /tests directory.

"""


def add_integer(a, b=98):
    """
        Function to add two integers.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
