#!/usr/bin/python3
"""
    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a prime
    number from the set and removing that number and its multiples from
    the set. The player that cannot make a move loses the game.
"""


def is_prime(num):
    # check if num is a prime number
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_game(n):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    remaining_numbers = set(range(1, n + 1))

    maria_turn = True
    while remaining_numbers:
        valid_moves = [p for p in primes if p in remaining_numbers]
        if not valid_moves:
            break

        move = max(valid_moves)
        remaining_numbers -= set(range(move, n + 1, move))
        maria_turn = not maria_turn
    return 'Maria' if maria_turn else 'Ben'


def isWinner(x, nums):
    """
        where x is the number of rounds and nums is an array of n
        Return: name of the player that won the most rounds
        If the winner cannot be determined, return None
        You can assume n and x will not be larger than 10000
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
