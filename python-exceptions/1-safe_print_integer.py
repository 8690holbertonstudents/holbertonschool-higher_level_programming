#!/usr/bin/python3
def safe_print_integer(value):
    if not value:
        return (False)
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return (True)
    except TypeError or ValueError:
        return (False)
