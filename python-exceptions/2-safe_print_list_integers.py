#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list:
        raise ValueError
    i = 0
    j = 0
    while i <= x - 1:
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except (IndexError, TypeError, ValueError):
            pass
        i += 1
    print()
    return (j)
