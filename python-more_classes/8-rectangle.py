#!/usr/bin/python3
"""
    Module to define class.
"""


class Rectangle:
    """
        Empty class named Rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object.

        Args:
            width: width of the the object Rectangle.
            height: height of the the object Rectangle.

        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """
        String representation of the Rectangle object.

        """
        if self.width == 0 or self.height == 0:
            return ("")
        my_str = ""
        for w in range(self.height):
            my_str += (str((self).print_symbol) * self.width) + "\n"
        my_str = my_str[:-1]
        return (my_str)

    def __repr__(self):
        """
        Python string representation of the Rectangle object.

        """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """
        Destructor for the Rectangle object.

        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """ function to calculate the area of Rectangle.

        Returns:
            Return the area of Rectangle.

        """
        return (self.width * self.height)

    def perimeter(self):
        """ function to calculate the perimeter of Rectangle.

        Returns:
            Return the perimeter of Rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return (rect_1)
        elif Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return (rect_2)
        else:
            return (rect_1)
