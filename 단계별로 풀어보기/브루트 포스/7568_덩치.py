n = int(input())
some_list = []
rank = ""

for i in range(n):
    split = input().split()
    some_list.append(split[0])
    some_list.append(split[1])

for i in range(0, len(some_list), 2):
    h = some_list[i]
    w = some_list[i + 1]
    count = 1

    for j in range(0, len(some_list), 2):
        h2 = some_list[j]
        w2 = some_list[j + 1]

        if int(h) < int(h2) and int(w) < int(w2):
            count += 1

    rank += str(count) + ' '

print(rank.rstrip())
