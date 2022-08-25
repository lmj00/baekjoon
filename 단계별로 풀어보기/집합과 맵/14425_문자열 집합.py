import sys

n, m = map(int, input().split())
n_dict = {sys.stdin.readline().rstrip() for i in range(n)}
m_list = [sys.stdin.readline().rstrip() for j in range(m)]
count = 0

for i in m_list:
    if i in n_dict:
        count += 1

print(count)