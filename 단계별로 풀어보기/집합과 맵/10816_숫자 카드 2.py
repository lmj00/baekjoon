from collections import Counter

input()
n_list = list(map(int, input().split()))
input()
m_list = list(map(int, input().split()))

counter = Counter(n_list)
[print(counter[i], end=' ') for i in m_list]