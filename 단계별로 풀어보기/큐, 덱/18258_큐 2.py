import sys
from collections import deque

ls = deque()

for i in range(int(input())):
    s = sys.stdin.readline().split()
    c = s[0]

    if c == 'push':
        ls.append(s[1])
    elif c == 'pop':
        ele = -1
        if ls:
            ele = ls.popleft()
        print(ele)
    elif c == 'size':
        print(len(ls))
    elif c == 'empty':
        if ls:
            print(0)
        else:
            print(1)
    elif c == 'front':
        ele = -1
        if ls:
            ele = ls[0]
        print(ele)
    else:
        ele = -1
        if ls:
            ele = ls[-1]
        print(ele)