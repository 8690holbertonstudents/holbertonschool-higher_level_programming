#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 != 0:
            print(f"Fizz ", end="")
        elif num % 3 != 0 and num % 5 == 0:
            print(f"Buzz ", end="")
        elif num % 3 == 0 and num % 5 == 0:
            print(f"FizzBuzz ", end="")
        else:
            print(f"{num} ", end="")
