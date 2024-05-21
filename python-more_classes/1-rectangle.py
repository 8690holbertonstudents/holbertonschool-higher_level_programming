#!/usr/bin/python3
"""
    Module to define class.
"""


class Rectangle:
    """
        Empty class named Rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object.

        Args:
            width: width of the the object Rectangle.
            height: height of the the object Rectangle.

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter function of width Rectangle.

        Returns:
            Return the width of Rectangle.

        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter function of width Rectangle.

        Args:
            value: Set value to Rectangle width.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be upper or equal to zero.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter function of height Rectangle.

        Returns:
            Return the height of Rectangle.

        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter function of height Rectangle.

        Args:
            value: Set value to Rectangle height.

        Raises:
            TypeError: height must be an integer.
            ValueError: height must be upper or equal to zero.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
