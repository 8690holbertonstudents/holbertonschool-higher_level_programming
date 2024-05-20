#!/usr/bin/python3
"""
    Python script for using doctest.
    Using a .txt file in /tests directory.

"""


def text_indentation(text):
    """
        function that prints a text with 2 new lines
         after each of these characters: . or ? or :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i <= (len(text) - 1):
        if ord(text[i]) != 46 \
           and ord(text[i]) != 58 \
           and ord(text[i]) != 63:
            print("{}".format(text[i]), end="")
        else:
            print("{}".format(text[i]))
            print()
            i += 1
        i += 1
    print()
