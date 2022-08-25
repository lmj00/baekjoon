import sys

co_list = []
[co_list.append(list(map(int, sys.stdin.readline().split()))) for i in range(int(input()))]
co_list.sort(key=lambda x: (x[1], x[0]))
for i in co_list:
    sys.stdout.write(f"{i[0]} {i[1]}\n")