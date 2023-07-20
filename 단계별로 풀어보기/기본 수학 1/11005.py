n, t = map(int, input().split())
ls = []

while n != 0:
    n, m = divmod(n, t)

    if m + 55 < 65:
        ls.append(m)
    else:
        ls.append(chr(m + 55))

print(*ls[::-1], sep='')