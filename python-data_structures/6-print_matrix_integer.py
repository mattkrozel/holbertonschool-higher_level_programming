#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        lengthrow = len(row)
        for i in range(lengthrow):
            if i != lengthrow - 1:
                print("{:d}".format(row[i]), end='')
            else:
                print("{:d}".format(row[i]), end='')
        print()
