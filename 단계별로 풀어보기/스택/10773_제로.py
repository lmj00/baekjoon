import sys

ls = []
for _ in range(int(input())):
    s = int(sys.stdin.readline())
    if s != 0:
        ls.append(s)
    else:
        del ls[-1]
print(sum(ls))