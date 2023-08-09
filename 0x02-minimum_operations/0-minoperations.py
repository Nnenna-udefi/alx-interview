#!/usr/bin/python3
"""Script involves finding the minimum number of operations required to
    generate a specific number of 'H' characters in a text file using
    the "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
        Code finds the prime factors of n and then calculate the sum
        of those prime factors to determine the mimumum no of operations

        no_operations: number of operations needed to generate 'n' 'H'
        characters
        n: factors to determine number of operations
    """
    if n == 1:
        return 0

    no_operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            no_operations += divisor
            n //= divisor
        else:
            divisor += 1
    return no_operations
