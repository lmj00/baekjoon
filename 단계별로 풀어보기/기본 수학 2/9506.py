while True:
    n = int(input())
    ls = []

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            ls.append(i)

    if n == sum(ls):
        print(f'{n} = ' + ' + '.join(map(str, ls)))
    else:
        print(f'{n} is NOT perfect.')