"""
The Coin Change Problem
Inputs: You are given an amount of money (N) and a list of coins such as C = ([1, 5, 10, 25])
Output: Define S(N, m, C) = How many ways to make change for N using only the first m coins in C?
    Gotcha: when indexing to find coin m, use C[m-1] because python indexes start at 0

Optimal substructure :robot: :

Assume I know the answers to S(1 ... N-1, 1...m, C). Then the answer to S(N, C) is the sum of two cases for each coin:

 - Case 1: Number of ways to make change for S without using any of coin m
    -> S(N, m-1, C)
 - Case 2: Use at least one of coin m to make change for S
    - > S(N-C[m], m, C)

Store S(N, m, C) in a table[N][m] (N+1) x (m+1)

Base cases:
 - if m == 0 -> table[:][0] = 0
 - if N == 0 -> table[0][:] = 1
"""


def count(N, m, coin_list):
    if m == 0:
        return 0
    smallest_coin = min(coin_list)
    if N == 0:
        return 1
    if N < smallest_coin:
        return 0

    memo = [list(-1 for idx in range(m + 1)) for idx in range(N + 1)]
    # Set up the base cases:
    for idx in range(N + 1):
        memo[idx][0] = 0
    for idx in range(m + 1):
        memo[0][idx] = 1
    for n in range(1, N + 1):
        for coin in range(1, m + 1):
            # S(N, m-1, C)
            case_1 = memo[n][coin - 1]
            # S(N-C[m-1], m, C)
            case_2 = memo[n - coin_list[coin - 1]][coin] if n - coin_list[
                coin - 1] >= 0 else 0
            memo[n][coin] = case_1 + case_2

    return memo[N][m]
