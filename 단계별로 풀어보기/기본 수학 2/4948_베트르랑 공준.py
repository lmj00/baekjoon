from math import sqrt, floor

while True:
    a = int(input())
    b = 2 * a + 1

    if a == 0:
        break

    some_list = []
    for i in range(2, b):
        some_list.append(i)

    j = 0
    k = 0
    count = 0
    prime = some_list[0]

    while j < floor(sqrt(b)):
        if some_list[k] != 0:
            prime = some_list[k]
            for i in range(prime * 2, b, prime):
                some_list[i - 2] = 0
            j += 1
        k += 1

    for i in some_list:
        if i > a:
            count += 1

    print(count)
