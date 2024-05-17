#!/usr/bin/python3
"""Python script to define class.
"""


class Square:
    """Create a class named Square.
    """
    def __init__(self, size=0):
        """Initialize the Square object.
        Args:
            size: Size of the the object Square.

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be upper or equal to zero.
        """
        self.__size = size
        if isinstance(self.__size, int) is False:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Fonction to calculate the area of Square.

            Returns:
                The value of area Square.
        """
        return (self.__size * self.__size)
