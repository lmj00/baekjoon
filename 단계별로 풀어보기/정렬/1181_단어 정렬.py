import sys

s_list = [(sys.stdin.readline().rstrip()) for i in range(int(sys.stdin.readline()))]
s_list = list(set(s_list))
s_list.sort()

if len(s_list[0]) != len(s_list[-1]):
    s_list.sort(key=len)
[print(i) for i in s_list]