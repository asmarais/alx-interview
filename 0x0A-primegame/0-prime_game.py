#!/usr/bin/python3
"""
0-prime_game
"""


def isWinner(x, nums):
    """
    Determines the winner of the most rounds
    between Maria and Ben.
    """
    max_n = max(nums)
    prime = [True for _ in range(max_n + 1)]
    prime[0], prime[1] = False, False
    p = 2

    while p * p <= max_n:
        if prime[p]:
            for i in range(p * p, max_n + 1, p):
                prime[i] = False
        p += 1

    def prime_count(n):
        """Returns the number of primes <= n."""
        return sum(prime[2:n+1])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = prime_count(n)
        if primes_in_game % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
