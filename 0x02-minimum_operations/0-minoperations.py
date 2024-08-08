#!/usr/bin/python3
""" Minimum Operations"""


def minOperations(n: int) -> int:
    """ Calculates the fewest number of operations to result in exactly n H characters """
    op = 0
    body = 'H'
    next = 'H'
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op
