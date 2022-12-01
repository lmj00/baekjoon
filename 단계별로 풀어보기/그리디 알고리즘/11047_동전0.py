k, money = map(int, input().split())

coin_list = []
coin_list += [int(input()) for i in range(k)]
count = 0
coin = 0
j = len(coin_list) - 1

while True:
    if money == 0:
        break

    if money >= coin_list[j]:
        coin = coin_list[j]
        count += money // coin
        money %= coin
    else:
        j -= 1

print(count)