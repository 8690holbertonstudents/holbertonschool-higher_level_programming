#!/usr/bin/python3
str = "a"
while str <= "z":
    print(str, end="")
    str = chr(ord(str) + 1)
