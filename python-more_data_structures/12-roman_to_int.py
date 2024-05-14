#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dictionnary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    i = 0
    end_string = (len(roman_string) - 1)
    while i <= end_string:
        cur_char = roman_string[i]
        if i != end_string:
            next_char = roman_string[i + 1]
        else:
            next_char = cur_char
        if cur_char in set(my_dictionnary.keys()):
            if my_dictionnary[next_char] > my_dictionnary[cur_char]:
                result -= my_dictionnary[cur_char]
            else:
                result += my_dictionnary[cur_char]
        i += 1
    return (result)
