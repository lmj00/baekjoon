a, b = map(int, input().split())

if b - 45 < 0:
    b = 60 + b - 45
    a -= 1

else:
    b = b - 45


if a < 0:
    a = 23

print(f"{a} {b}")
