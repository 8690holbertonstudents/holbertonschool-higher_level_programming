#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    count = 0
    for char in str:
        if count != n and n >= 0:
            str2 += char
        elif n < 0:
            str2 = str
        count += 1
    return str2
