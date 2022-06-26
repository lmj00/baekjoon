some_list = [int(input()) for i in range(10)]
rest_list = [str(i % 42) for i in some_list]

final_list = []

for i in rest_list:
    if i not in final_list:
        final_list.append(i)

print(len(final_list))
