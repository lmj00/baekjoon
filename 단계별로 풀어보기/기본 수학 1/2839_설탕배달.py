num = int(input())
i = 0
check = -1

while i <= num:
    j = 0
    while j <= num:
        if i + j == num:
            check = i // 3 + j // 5
            i = num
            break

        j += 5
    i += 3
print(check)
