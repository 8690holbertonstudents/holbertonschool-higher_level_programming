#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append([])
        for num in row:
            new_matrix[-1].append(num * num)
    return (new_matrix)
