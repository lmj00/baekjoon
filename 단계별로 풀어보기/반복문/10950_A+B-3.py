t = int(input())
some_list = []

for i in range(t):
    a, b = map(int, input().split())
    some_list.append(a + b)

for i in some_list:
    print(i)