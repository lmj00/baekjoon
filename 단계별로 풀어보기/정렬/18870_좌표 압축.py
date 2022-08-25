import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
co_list = list(map(int, sys.stdin.readline().split()))
some_list = list(co_list)
co_list = list(set(co_list))
co_list.sort()

s = []
s += [bisect_left(co_list, i) for i in some_list]
print(*s)