import sys

n, m = map(int, input().split())
a = {sys.stdin.readline().rstrip() for _ in range(n)}
b = [sys.stdin.readline().rstrip() for _ in range(m)]
count = 0
s_list = []

for i in b:
    if i in a:
        count += 1
        s_list.append(i)

print(count)
s_list.sort()
[print(j) for j in s_list]