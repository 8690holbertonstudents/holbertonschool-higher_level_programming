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
    end = (len(text) - 1)
    while i <= end:
        if ord(text[i]) == 46 \
           or ord(text[i]) == 58 \
           or ord(text[i]) == 63:
            print("{}".format(text[i]))
            print()
            if ord(text[i + 1]) == 32 and i != end:
                i += 1
        else:
            print("{}".format(text[i]), end="")
        i += 1
