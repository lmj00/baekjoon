co_list = []
[co_list.append(list(map(int, input().split()))) for i in range(int(input()))]
co_list.sort()
for i in co_list:
    print(f"{i[0]} {i[1]}")
