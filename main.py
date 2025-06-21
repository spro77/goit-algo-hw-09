def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        count, amount = divmod(amount, coin)
        if count:
            result[coin] = count

    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [(float('inf'), None)] * (amount + 1)
    min_coins[0] = (0, None)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin][0] + 1 < min_coins[i][0]:
                min_coins[i] = (min_coins[i - coin][0] + 1, coin)

    res = {}
    i = amount

    while i > 0:
        coin = min_coins[i][1]
        res[coin] = res.get(coin, 0) + 1
        i -= coin
    return res


def main():
    amount = int(input("Введіть суму: "))
    greedy_result = find_coins_greedy(amount)
    min_coins_result = find_min_coins(amount)

    print("Жадібний алгоритм:      ", greedy_result)
    print("Динамічне програмування:", min_coins_result)


if __name__ == "__main__":
    main()