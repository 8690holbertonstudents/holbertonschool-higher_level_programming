#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        j = 0
        while i <= x - 1:
            if isinstance(my_list[i], int):
                print("{}".format(my_list[i]), end="")
                j += 1
            i += 1
        print()
    except IndexError or TypeError:
        print()
    return (j)
