import sys

for i in range(int(sys.stdin.readline())):
    s = input().split()
    [print(j[::-1], end=' ') for j in s]