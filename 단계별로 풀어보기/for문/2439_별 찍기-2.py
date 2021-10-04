a = int(input())
star = ""
star2 = ""

for i in range(a):
    star += "*"

    for j in range(i + 1, a):
        star2 += " "

    print(star2 + star)
    star2 = ""
