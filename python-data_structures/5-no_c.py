#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for _char in my_string:
        if ord(_char) != 67 and ord(_char) != 99:
            new_string += _char
    return (new_string)
