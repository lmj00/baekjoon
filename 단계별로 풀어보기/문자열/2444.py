n = int(input())

ls = [i for i in range(1, n * 2, 2)]
ls += ls[::-1][1:]
j = 1

for star in ls:
    print(" " * (abs(n - j)) + "*" * star)
    j += 1