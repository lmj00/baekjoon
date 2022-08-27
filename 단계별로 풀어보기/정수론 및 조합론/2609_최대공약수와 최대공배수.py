a, b = map(int, input().split())
min_v = min(a, b)
mul = 0

for i in range(1, min_v + 1):
    if a % i == 0 and b % i == 0:
        mul = i
print(mul)
print(a // mul * b // mul * mul)