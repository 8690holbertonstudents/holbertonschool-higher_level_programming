#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    for tuple in my_list:
        score += tuple[0] * tuple[1]
        weight += tuple[1]
    result = score / weight
    return (result)
