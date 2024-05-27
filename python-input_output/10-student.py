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

    def to_json(self, attrs=None):
        """
            Function that returns the dictionary representation
            of a Student instance.

            Returns:
            the dictionary description.
        """
        My_dict = {}

        if isinstance(attrs, list):
            flag = True
        else:
            flag = False

        for key, data in self.__dict__.items():
            if flag:
                for val in attrs:
                    if val == key:
                        My_dict[key] = data
            else:
                My_dict[key] = data

        return (My_dict)
