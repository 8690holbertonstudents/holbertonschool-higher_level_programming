#!/usr/bin/python3
"""
    Module to use abstract class.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
        Abstract class named Shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method named area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method named perimeter.
        """
        pass


class Circle(Shape):
    """
        Subclass named Circle inherit from Shape.
    """

    def __init__(self, radius):
        """Initialize the Circle object.

        Args:
            radius: radius of the the object Circle.

        """
        self.radius = radius

    def area(self):
        """
        Method to caclulate the area of a circle.

        Returns:
        The calculated area.

        """
        return (abs(math.pi * ((self.radius) ** 2)))

    def perimeter(self):
        """
        Method to caclulate the perimeter of a circle.

        Returns:
        The calculated perimeter.

        """
        return (abs(2 * math.pi * self.radius))


class Rectangle(Shape):
    """
        Subclass named Rectangle inherit from Shape.
    """

    def __init__(self, width, height):
        """Initialize the Rectangle object.

        Args:
            width: width of the the object Rectangle.
            height: height of the the object Rectangle.

        """
        self.width = width
        self.height = height

    def area(self):
        """
        Method to caclulate the area of a rectangle.

        Returns:
        The calculated area.

        """
        return (abs(self.width * self.height))

    def perimeter(self):
        """
        Method to caclulate the perimeter of a rectangle.

        Returns:
        The calculated perimeter.

        """
        return (abs(2 * (self.width + self.height)))


def shape_info(s_info):
    """
    Method to print area and perimeter of a shape.

    Returns:
    Print the Area and Perimeter values.

    """
    print(f"Area: {s_info.area()}")
    print(f"Perimeter: {s_info.perimeter()}")
