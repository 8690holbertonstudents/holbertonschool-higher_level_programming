#!/usr/bin/python3*
"""
    Module To use serialisation in python.
"""
import pickle


class CustomObject:
    """
        Class object named CustomObject.
    """

    def __init__(self, name, age, is_student):
        """Initialize CustomObject.

        Args:
            name: a string that represent the name of student.
            age: an integer represent the age of studend.
            is_student: a boolean for student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
            Method to print object attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Method take a filename as its parameter. Using the pickle module,
         it will serialize the current instance of the object,
         and save it to the provided filename.

        Args:
            filename: The name of file to create with pickle.

        Returns:
            The filename with serialized data.
        """
        try:
            with open(filename, mode="wb") as My_File:
                pickle.dump(self, My_File)
        except (FileExistsError,FileNotFoundError):
            return (None)

    @classmethod
    def deserialize(cls, filename):
        """
        Class method take a filename as its parameter.
        Using the pickle module, it will load and return
        an instance of the CustomObject from the provided filename.

        Args:
            filename: The name of file to load with pickle.

        Returns:
            The Python dictionary.
        """
        try:
            with open(filename, mode="rb") as My_File:
                return (pickle.load(My_File))
        except (FileExistsError,FileNotFoundError):
            return (None)
