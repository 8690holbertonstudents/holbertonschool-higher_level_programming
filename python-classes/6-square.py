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
        self.__size = size
        self.__position = position

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
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
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
        if isinstance(value, tuple) is False \
           or len(value) != 2 \
           or value[0] < 0 or value[1] < 0 \
           or isinstance(value[0], int) is False \
           or isinstance(value[1], int) is False:
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
        if self.__position[1] > 0:
            print("")

        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for val in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
