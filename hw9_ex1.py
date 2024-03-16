import timeit

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    coin_count = {}
    for coin in coins:
        count = amount // coin
        if count:
            coin_count[coin] = count
        amount %= coin
    return coin_count

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    result = {}
    while amount > 0:
        for coin in coins:
            if amount - coin >= 0 and dp[amount] == dp[amount - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break

    return result

amount = 113
greedy_result = find_coins_greedy(amount)
dp_result = find_min_coins(amount)

print(greedy_result)
print(dp_result)

greedy_time = timeit.timeit('find_coins_greedy(10009)', globals=globals(), number=1000)
dp_time = timeit.timeit('find_min_coins(10009)', globals=globals(), number=1000)

print(f"Час виконання жадібного алгоритму: {greedy_time} секунд")
print(f"Час виконання алгоритму динамічного програмування: {dp_time} секунд")