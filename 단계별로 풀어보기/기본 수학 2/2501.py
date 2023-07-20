n, k = map(int, input().split())
ls = []

for i in range(1, n + 1):
    if n % i == 0:
        ls.append(i)

print(ls[k - 1]) if len(ls) >= k else print(0)