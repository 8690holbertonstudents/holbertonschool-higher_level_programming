#!/usr/bin/python3
"""
    Module to explore multiple inheritance in class (MRO).
"""


class Fish:
    """
        A Class named Fish.
    """

    def swim(self):
        """
        Method to print the "The fish is swimming".
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Method to print the "The fish lives in water".
        """
        print("The fish lives in water")


class Bird:
    """
        A Class named Bird.
    """

    def fly(self):
        """
        Method to print the "The bird is flying".
        """
        print("The bird is flying")

    def habitat(self):
        """
        Method to print the "The bird lives in the sky".
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
        A Subclass named FlyingFish that inherits
        from Fish and Bird classes.
    """

    def fly(self):
        """
        Method to override the fly method.
        print "The bird is flying".
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Method to override the swim method.
        print "The flying fish is swimming!".
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Method to override the swim method.
        print "The flying fish lives both in water and the sky!".
        """
        print("The flying fish lives both in water and the sky!")
