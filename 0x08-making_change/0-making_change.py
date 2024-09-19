#!/usr/bin/python3
""" Making changes """

def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range (coin, total + 1):
            dp[amount] = min(dp[amount], (dp[amount - coin] + 1))
    
    return dp[total] if dp[total] != total + 1 else -1

print(makeChange([1, 2, 25], 37))  # Output: 4 (25 + 10 + 2)
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1 (not possible)