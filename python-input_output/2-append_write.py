#!/usr/bin/python3
"""
    Module to append to a text file.
"""


def append_write(filename="", text=""):
    """
        Function to append at the end of a text file (UTF8).

        Args:
         filename: The filename to create / append to.
         text: The text to write in the file.

        Returns:
         The numbers of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as My_File:
        read_data = My_File.write(text)
        return (len(text))
