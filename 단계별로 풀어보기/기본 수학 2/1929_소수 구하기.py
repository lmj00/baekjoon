from math import sqrt, floor

a, b = map(int, input().split())
some_list = []
for i in range(2, b + 1):
    some_list.append(i)

value = floor(sqrt(b))
j = 0
k = 0
prime = some_list[0]

while j < value:
    if some_list[k] != 0:
        prime = some_list[k]
        for i in range(prime * 2, b + 1, prime):
            some_list[i - 2] = 0
        j += 1
    k += 1


for i in some_list:
    if i >= a:
        print(i)