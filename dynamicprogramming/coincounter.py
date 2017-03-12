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
