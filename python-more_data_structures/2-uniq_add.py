#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_result = 0
    for num in set(my_list):
        add_result += num
    return (add_result)
