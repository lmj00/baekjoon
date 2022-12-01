input()
time = list(map(int, input().split()))
time.sort()
value = 0

for i in range(len(time)):
    value += sum(time[:i + 1])

print(value)