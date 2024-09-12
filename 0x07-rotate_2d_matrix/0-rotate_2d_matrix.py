#!/usr/bin/python3
"""Module Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Given a 2D matrix, rotate it 90 degrees clockwise."""
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
