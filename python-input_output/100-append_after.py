#!/usr/bin/python3
"""
    Python script to manipulate file I/O.
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Function that inserts a line of text to a file,
        after each line containing a specific string.

        Args:
            filename: the filename to open and write in.
            search_string: the string to find in the text file.
            new_string:
    """
    with open(filename, mode="r", encoding="utf-8") as My_File:
        lines = My_File.readlines()

        output = []
        for line in lines:
            output.append(line)
            if line.find(search_string) != -1:
                output.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as My_File:
        My_File.writelines(output)
