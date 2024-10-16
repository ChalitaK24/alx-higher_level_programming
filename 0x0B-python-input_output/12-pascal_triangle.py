#!/usr/bin/python3
"""
Function listing pascal's triangle of n
"""


def pascal_triangle(n):
    """
    n(int): number of rows
    Returns: list
    """
    if n <= 0:
        return[]

    triangle = [[1]]

    for i in range(1, n):
        row_prv = tri[-1]
        row = [1] + [row_prv[j] + row_prv[j + 1]
                       for j in range(len(row_prv) - 1)] + [1]
        triangle.append(row)
    return triangle
