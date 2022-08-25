import sys

s_list = [sys.stdin.readline().rstrip().split() for i in range(int(input()))]
s_list.sort(key=lambda x: (int(x[0])))
[sys.stdout.write(f"{i[0]} {i[1]}\n") for i in s_list]