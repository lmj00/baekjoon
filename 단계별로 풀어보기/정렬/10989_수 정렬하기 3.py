import sys

s_list = [0] * 10001
n = int(input())
for i in range(n):
    s_list[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for j in range(s_list[i]):
        print(i)