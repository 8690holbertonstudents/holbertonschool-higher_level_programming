#!/usr/bin/python3
"""
    Module to define subclasses.
"""


class MyList(list):
    """
        Class named Mylist inherit from List.
    """
    def print_sorted(self):
        """
        prints the list in ascending order.
        """
        print(sorted(self))
