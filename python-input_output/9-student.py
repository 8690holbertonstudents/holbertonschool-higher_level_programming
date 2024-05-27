#!/usr/bin/python3
"""
    Module to manipulate class.
"""


class Student():
    """
        A class object named Student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize the Student object.

        Args:
            first_name: First name of Student.
            last_name: Last name of Student.
            age: age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Function that returns the dictionary representation
            of a Student instance.

            Returns:
            the dictionary description.
        """
        return (self.__dict__)
