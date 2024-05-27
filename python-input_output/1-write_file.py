#!/usr/bin/python3
"""
    Module to write to a text file.
"""


def write_file(filename="", text=""):
    """
        Function to write to  a text file (UTF8).

        Args:
         filename: The filename to create.
         text: The text to write in the file.

        Returns:
         The numbers of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as My_File:
        read_data = My_File.write(text)
        return (len(text))
