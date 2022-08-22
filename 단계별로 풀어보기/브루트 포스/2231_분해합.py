num = int(input())
i = 0

for i in range(1, num + 1):
    value = 0
    for j in str(i):
        value += int(j)

    if value + i == num:
        print(i)
        break

if i == num:
    print(0)

