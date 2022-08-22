h, m = map(int, input().split())
m2 = m + int(input())

if m2 >= 60:
    h2 = m2 // 60 + h
    if h2 > 23:
        h2 -= 24
    m3 = m2 % 60
    print(f"{h2} {m3}")
else:
    print(f"{h} {m2}")
