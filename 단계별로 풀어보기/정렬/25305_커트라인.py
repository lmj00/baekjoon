N, k = map(int, input().split())
s_list = list(map(int, input().split()))
s_list.sort(reverse=True)
print(s_list[k - 1])