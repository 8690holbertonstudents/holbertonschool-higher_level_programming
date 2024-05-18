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
        self.__size = value
        if isinstance(self.__size, int) is False:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

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
        self.__position = value
        if isinstance(self.__position, tuple) is False or \
            len(self.__position) != 2 or \
                self.__position[0] < 0 or \
                self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Fonction to calculate the area of Square.

            Returns:
                The value of area Square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Fonction to print Square size.

            >>> print: character # represent Square size.
                with space before represent by Square Position.
        """
        if self.__size == 0:
            print()
        else:
            for r_size in range(self.__size):
                for space in range(self.__position[0]):
                    print(f" ", end="")
                for c_size in range(self.__size):
                    print(f"#", end="")
                print()
