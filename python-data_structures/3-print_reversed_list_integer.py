#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for _int in my_list:
        print("{:d}".format(_int))
