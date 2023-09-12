#!/usr/bin/python3
"""script that rotates a 2d matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """n is the number of rows/columns in the matrix"""
    n = len(matrix)

    # swap elements across the main diagonal of the matrix
    # (from top-left to bottom-right)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row 90 degrees clockwise
    for i in range(n):
        matrix[i] = matrix[i][::-1]
