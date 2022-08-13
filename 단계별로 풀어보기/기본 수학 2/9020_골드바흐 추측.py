count = int(input())

for i in range(count):
    num = int(input())
    v1 = num // 2
    v2 = v1
    check = v1 - 1

    while True:
        if v1 + v2 == num:
            for j in range(2, v1):
                check = j
                if v1 % j == 0:
                    break
                elif v2 % j == 0:
                    break
        if check == v1 - 1:
            print(f"{v1} {v2}")
            break

        v1 -= 1
        v2 += 1