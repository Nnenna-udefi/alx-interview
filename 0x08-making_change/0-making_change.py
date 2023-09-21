#!/usr/bin/python3
"""script determine the fewest number of coins needed to meet a given amount
"""


def makeChange(coins, total):
    """
        float('inf'): represents positive infinity in Python.
        [float('inf')]: creates a list with a single element
        * (total + 1): duplicates this list total + 1 times,
        creating a list of length total + 1
        where each element is positive infinity.
    """
    if total <= 0:
        return 0

    # Initialize a table to store the minimum number
    # of coins needed for each amount from 0 to total
    length = total + 1
    value = [float('inf')] * (length)
    value[0] = 0

    for coin in coins:
        for amount in range(coin, length):
            # Update the minimum number of coins needed for the current amount
            value[amount] = min(value[amount], value[amount - coin] + 1)

    if value[total] == float('inf'):
        return -1

    return value[total]
