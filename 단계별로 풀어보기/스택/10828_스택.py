import sys
ls = []

for i in range(int(input())):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        ls.append(s[1])
    elif s[0] == 'pop':
        ele = -1
        if len(ls) != 0:
            ele = ls[-1]
            del ls[-1]
        print(ele)
    elif s[0] == 'size':
        print(len(ls))
    elif s[0] == 'empty':
        if ls:
            print(0)
        else:
            print(1)
    else:
        if ls:
            print(ls[-1])
        else:
            print(-1)