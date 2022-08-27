while True:
    n = list(map(int, input().split()))
    n.sort()
    if n[0] + n[1] + n[2] == 0:
        break
    print('right') if n[0] ** 2 + n[1] ** 2 == n[2] ** 2 else print('wrong')