from bisect import bisect_left, bisect_right

input()
n_list = list(map(int, input().split()))
n_list.sort()

input()
m_list = list(map(int, input().split()))

for i in m_list:
    if bisect_right(n_list, i) - bisect_left(n_list, i) > 0:
        print(1, end=' ')
    else:
        print(0, end=' ')
