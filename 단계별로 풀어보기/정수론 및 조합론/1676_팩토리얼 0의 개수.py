n = 1
for i in range(2, int(input()) +1):
    n *= i
n = str(n)

count = 0
for i in range(len(n) - 1, 0, -1):
    if n[i] != '0':
        break
    count += 1
print(count)