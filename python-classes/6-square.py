#!/usr/bin/python3
"""Python script to define class.
"""


class Square:
    """Create a class named Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square object.

        Args:
            size: Size of the the object Square.
            position: Position of the the object Square.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter function of size Square.

        Returns:
            Return the size of Square.

        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter function of size Square.

        Args:
            value: Set value to Square size.

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be upper or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter function of position Square.

        Returns:
            Return the position of Square.

        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter function of position Square.

        Args:
            value: Set value to Square position.

        Raises:
            TypeError: position must be a tuple
            of two positives integer values.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(x, int) for x in value) \
           or any(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Fonction to calculate the area of Square.

            Returns:
                The value of area Square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Fonction to print Square.

            >>> print: character # represent Square size.
                with space before represent by Square Position.
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for j in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
