#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
        if isinstance(self.__size, int) is False:
            raise ValueError("size must be an integer")
        elif self.__size < 0:
            raise TypeError("size must be >= 0")
