from collections import Counter

x_list = []
y_list = []
for i in range(3):
    s = input().split()
    x_list.append(int(s[0]))
    y_list.append(int(s[1]))

x = Counter(x_list).most_common()
y = Counter(y_list).most_common()

for i in range(len(x)):
    if x[i][1] % 2 == 1:
        print(x[i][0], end=' ')
    if y[i][1] % 2 == 1:
        print(y[i][0])