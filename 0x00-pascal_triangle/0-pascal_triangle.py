#!/usr/bin/python3
"""prints pascals triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
        representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    c = [[1]]
    for i in range(1, n):
        prev_row = c[-1]
        curr_row = [1]
        for j in range(1, len(prev_row)):
            curr_row.append(prev_row[j - i] +
                            prev_row[j])
        curr_row.append(1)
        c.append(curr_row)
    return c
