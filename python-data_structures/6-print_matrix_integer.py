#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        space = " "
        for j in range(len(matrix[i])):
            if j == (len(matrix[i]) - 1):
                space = ""
            print("{:d}{}".format(matrix[i][j], space), end="")
        print()
