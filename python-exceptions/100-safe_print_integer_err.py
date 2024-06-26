#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError):
        msg = "Exception: Unknown format code 'd' for object of type 'str'"
        print(msg, file=sys.stderr)
        return (False)
    return (True)
