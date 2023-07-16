n, m = map(int, input().split())
b = [0] * n

for _ in range(m):
    v = list(map(int, input().split()))

    for i in range(v[0] - 1, v[1]):
        b[i] = v[2]

print(*b)