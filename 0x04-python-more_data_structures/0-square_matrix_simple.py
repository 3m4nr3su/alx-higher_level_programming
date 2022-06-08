#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = list()

    def square(x):
        return (x * x)
    for i in matrix:
        y = list(map(square, i))
        result.append(y)
    return result
