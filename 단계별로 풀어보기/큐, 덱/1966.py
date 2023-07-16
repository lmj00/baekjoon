from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    r = input().rstrip().split(' ')
    dq_ranks = deque(input().rstrip().split(' '))
    idx = int(r[1])

    while True:
        if max(dq_ranks) == dq_ranks[idx] and idx == 0:
            break
        elif dq_ranks[0] == max(dq_ranks):
            dq_ranks.popleft()
        else:
            dq_ranks.append(dq_ranks.popleft())

        idx -= 1

        if idx == -1:
            idx = len(dq_ranks) - 1

    print(int(r[0]) - len(dq_ranks) + 1)