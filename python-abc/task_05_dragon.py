#!/usr/bin/python3
"""
    Module to mastering mixins classes.
"""


class SwimMixin:
    """
        A Class named SwimMixin.
    """

    def swim(self):
        """
        Method to print the "The creature swims!".
        """
        print("The creature swims!")

    def fly(self):
        """
        Method to print the "The creature flies!".
        """
        print("The creature flies!")


class FlyMixin:
    """
        A Class named FlyMixin.
    """

    def swim(self):
        """
        Method to print the "The creature swims!".
        """
        print("The creature swims!")

    def fly(self):
        """
        Method to print the "The creature flies!".
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
        A Subclass named Dragon that inherits
        from SwimMixin and FlyMixin classes.
    """

    def roar(self):
        """
        Method to print the "The dragon roars!".
        """
        print("The dragon roars!")

    def breath(self):
        """
        Method to print the "The dragon breathes fire!".
        """
        print("The dragon breathes fire!")

    def master_of(self):
        """
        Method to print the "The Master of Dragons: Smaug!".
        """
        print("The Master of Dragons: Smaug!")
