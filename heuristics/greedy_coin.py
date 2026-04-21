def greedy_coin(change):
    coins = [25, 10, 5, 1]
    result = {}

    for coin in coins:
        count = int(change // coin)
        result[coin] = count
        change -= coin * count

    return result