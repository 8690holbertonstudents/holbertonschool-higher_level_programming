#!/usr/bin/python3
"""
    Module to manipulate subclasses.
"""


class BaseGeometry:
    """
        Empty class named BaseGeometry.
    """
    def area(self):
        """ function to calculate the area of BaseGeometry.

        Returns:
            Return exception cause area is not implemented.

        """
        raise Exception("area() is not implemented")
