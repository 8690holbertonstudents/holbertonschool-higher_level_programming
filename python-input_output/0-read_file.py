#!/usr/bin/python3
"""
    Module to read from a text file.
"""


def read_file(filename=""):
    """
        Function to read a text file (UTF8) and prints to stdout.

        Args:
         filename: The file to open.

        Returns:
         The entire file content.
    """
    with open(filename, mode="r", encoding="utf-8") as My_File:
        read_data = My_File.read()
        print(read_data, end="")
