#!/usr/bin/python3
"""
    Module to use abstract class.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
        Abstract class named Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method named sound.
        """
        pass


class Dog(Animal):
    """
        Subclass named Dog inherit from Animal.
    """

    def sound(self):
        """
        Method named sound : Sound of a dog.
        """
        self.sound = "Bark"
        return (self.sound)


class Cat(Animal):
    """
        Subclass named Cat inherit from Animal.
    """

    def sound(self):
        """
        Method named sound : Sound of a cat.
        """
        self.sound = "Meow"
        return (self.sound)
