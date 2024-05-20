#!/usr/bin/python3
"""
    Python script for using doctest.
    Using a .txt file in /tests directory.

"""


def matrix_divided(matrix, div):
    """
        Function to divide all elements of a matrix.
    """
    if not isinstance(matrix, list) \
       or not all(isinstance(row, list) for row in matrix) \
       or not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for val in row:
            new_row.append(round((val / div), 2))
        new_matrix.append(new_row)
    return (new_matrix)
