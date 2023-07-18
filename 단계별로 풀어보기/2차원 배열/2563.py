v = [[0 for _ in range(100)] for _ in range(100)]
result = 0

for i in range(int(input())):
    a, b = map(int, input().split())

    for j in range(10):
        for k in range(10):
            v[b + k][a + j] = 1

for i in v:
    result += i.count(1)

print(result)