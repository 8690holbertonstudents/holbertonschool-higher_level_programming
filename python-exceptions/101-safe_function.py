#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except ZeroDivisionError:
        msg = "Exception: division by zero"
        print(msg, file=sys.stderr)
    except IndexError:
        msg = "Exception: list index out of range"
        print(msg, file=sys.stderr)
        return (None)
