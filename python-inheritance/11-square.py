#!/usr/bin/python3
"""
    Module to manipulate subclasses.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Subclass Square inherit from class Rectangle.

        Args:
            size: size of subclass Square.
    """

    def __init__(self, size):
        self.__size = size

        self.integer_validator("size", size)

    def area(self):
        """ function to calculate the area of Square.

        Returns:
            Return the area of Square.

        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        String representation of the Square object.

        """
        return (f"[Square] {self.__size}/{self.__size}")
