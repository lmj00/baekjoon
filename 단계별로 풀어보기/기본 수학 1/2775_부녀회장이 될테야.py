num = int(input())
some_list = []

for i in range(num):
    k = int(input())
    n = int(input())

    for j in range(1, n + 1):
        some_list.append(j)

    for l in range(k):
        for l2 in range(1, n):
            some_list[l2] = some_list[l2 - 1] + some_list[l2]

    print(some_list[n - 1])
    some_list.clear()