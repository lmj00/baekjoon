from collections import Counter

for i in range(int(input())):
    s_list = []
    count = 1
    for j in range(int(input())):
        s_list.append(input().split()[1])

    common = Counter(s_list).most_common()
    for k in range(len(common)):
        count *= common[k][1] + 1
    print(count - 1)