import sys

N, M = map(int, input().split())
num_ls = list(map(int, input().split()))

for j in range(len(num_ls) - 1):
    num_ls[j + 1] += num_ls[j]
num_ls.insert(0, 0)

for _ in range(M):
    f, s = map(int, sys.stdin.readline().split())
    f_v = num_ls[f - 1]
    s_v = num_ls[s]

    print(s_v - f_v)
