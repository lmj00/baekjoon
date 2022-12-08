from collections import deque
import sys

dq = deque()

for i in range(int(input())):
    s = sys.stdin.readline().split()
    c = s[0]

    if c == 'push_front':
        dq.insert(0, s[1])
    elif c == 'push_back':
        dq.append(s[1])
    elif c == 'pop_front':
        val = -1
        if dq:
            val = dq.popleft()
        print(val)
    elif c == 'pop_back':
        val = -1
        if dq:
            val = dq.pop()
        print(val)
    elif c == 'size':
        print(len(dq))
    elif c == 'empty':
        val = 1
        if dq:
            val = 0
        print(val)
    elif c == 'front':
        val = -1
        if dq:
            val = dq[0]
        print(val)
    else:
        val = -1
        if dq:
            val = dq[-1]
        print(val)