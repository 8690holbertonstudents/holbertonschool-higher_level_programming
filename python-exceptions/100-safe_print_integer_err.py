#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    if not value:
        raise ValueError
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        msg = "Exception: Unknown format code 'd' for object of type 'str'"
        print(msg, file=sys.stderr)
        return (False)
