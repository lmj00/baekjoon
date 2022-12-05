from collections import deque
import sys

N = int(input())
dq = deque()

while True:
    num = int(sys.stdin.readline())

    if num == -1:
        break
    elif num == 0:
        dq.popleft()
    else:
        if len(dq) < N:
            dq.append(num)

if len(dq) == 0:
    print("empty")
else:
    [print(i, end=' ') for i in dq]