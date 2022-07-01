num = int(input())
pivot = 2
i = 1

while True:
    if 6 * i + 1 >= num:
        break
    i += pivot
    pivot += 1

print(1) if num == 1 else print(pivot)
