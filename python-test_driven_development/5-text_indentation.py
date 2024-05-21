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

    flag = 0
    for i in range(len(text)):
        if text[i] == ' ' and flag == 1:
            continue
        if text[i] in set(".?:"):
            print("{}".format(text[i]))
            print()
            flag = 1
        else:
            print("{}".format(text[i]), end="")
            flag = 0
