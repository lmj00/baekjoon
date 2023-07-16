n, m = map(int, input().split())
b = [i + 1 for i in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    b = b[:v1 - 1] + b[v1 - 1:v2][::-1] + b[v2:]

print(*b)