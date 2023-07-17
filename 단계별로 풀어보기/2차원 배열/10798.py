a = [[' ' for _ in range(15)] for _ in range(5)]

for i in range(5):
    v = input()
    for j in range(len(v)):
        a[i][j] = v[j]

for i in range(15):
    for j in range(5):
        if a[j][i] != ' ':
            print(a[j][i], end='')