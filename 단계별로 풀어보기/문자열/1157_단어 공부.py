word = list(input().lower())

some_list = []
spelling = list(set(word))
count = 0

for i in spelling:
    some_list.append(word.count(i))

max_count = max(some_list)
for j in some_list:
    if j == max_count:
        count += 1

if count > 1:
    print("?")
else:
    index = some_list.index(max_count)
    print(str(spelling[index]).upper())

