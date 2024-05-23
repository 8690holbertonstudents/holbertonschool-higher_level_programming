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

    def integer_validator(self, name, value):
        """Function to validate argument value.

        Args:
            value: Verify if value is an integer..

        Raises:
            TypeError: value must be an integer.
            ValueError: value must be upper than zero.

        """
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
