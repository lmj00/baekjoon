a, b, c = map(int, input().split())
v = max(a, b, c)

if a == b == c:
    print(10000 + v * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(v * 100)
