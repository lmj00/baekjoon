import sys

N, M = map(int, input().split())
pocket_list = {}
for i in range(1, N + 1):
    pocket_list[i] = sys.stdin.readline().rstrip()

d = dict((v, k) for (k, v) in pocket_list.items())

for i in range(M):
    answer = sys.stdin.readline().rstrip()
    if 64 < ord(answer[0]) < 91 or 64 < ord(answer[-1]) < 91:
        print(d[answer])
    else:
        print(pocket_list[int(answer)])