#!/usr/bin/python3
for digit_D in range(0, 9):
    for digit_U in range((digit_D + 1), 10):
        if digit_D == 8 and digit_U == 9:
            print("{}".format(89))
        else:
            print("{}{}, ".format(digit_D, digit_U), end="")
