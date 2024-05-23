#!/usr/bin/python3
"""
    Module to manipulate subclasses.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Subclass Rectangle inherit from class BaseGeometry.

        Args:
            width: width of subclass Rectangle.
            height: height of subclass Rectangle.
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
