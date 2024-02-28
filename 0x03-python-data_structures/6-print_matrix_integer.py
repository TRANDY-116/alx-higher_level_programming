#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    print("{:d}".format(matrix[i][j]), end="")
    if j != (len(matrix[i]) - 1):
        print(" ", end="")
        print("")
