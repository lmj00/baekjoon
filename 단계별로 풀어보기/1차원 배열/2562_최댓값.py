some_list = []

for i in range(9):
    some_list.append(int(input()))

print(max(some_list))
print(some_list.index(max(some_list)) + 1)
