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
            Method that returns the dictionary representation
            of a Student instance.

            Returns:
            the dictionary description.
        """
        My_dict = {}

        if isinstance(attrs, list):
            flag = True
        else:
            flag = False

        for key, value in self.__dict__.items():
            if flag:
                for val in attrs:
                    if val == key:
                        My_dict[key] = value
            else:
                My_dict[key] = value

        return (My_dict)

    def reload_from_json(self, json):
        """
            Method that replace all attributes
            of Student instance.

            Args:
                json: A dictionary.

            Returns:
            update attributes.
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
