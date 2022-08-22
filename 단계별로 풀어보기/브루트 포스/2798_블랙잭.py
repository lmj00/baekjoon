N, M = map(int, input().split())
some_list = list(map(int, input().split()))
some_list.sort()
value = []

for i in range(len(some_list)):
    for j in range(i + 1, len(some_list)):
        for k in range(j + 1, len(some_list)):
            num = some_list[i] + some_list[j] + some_list[k]
            if num <= M:
                value.append(num)

value.sort()
print(value[-1])