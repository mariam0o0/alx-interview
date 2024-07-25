#!/usr/bin/python3
"""0-pascal_triangle"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    output = []
    if n <= 0:
        return output
    for i in range(n):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(output[i-1][j-1] + output[i-1][j])
        output.append(temp)
    return output
