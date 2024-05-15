#!/usr/bin/python3
def safe_print_integer(value):
    if not value:
        raise ValueError
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
