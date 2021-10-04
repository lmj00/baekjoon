seq, pivot = map(int, input().split())

some_list = map(int, input().split())

for i in some_list:
    if i < pivot:
        print(i, end=' ')
