from collections import deque

N, K = map(int, input().split())
dq = deque([i for i in range(1, N + 1)])
ls = []

for _ in range(N):
    dq.rotate(-K)
    ls.append(dq[-1])
    dq.remove(dq[-1])

print(f"<", end='')
[print(f"{ls[i]}, ", end='') for i in range(len(ls) - 1)]
print(f"{ls[-1]}>", end='')