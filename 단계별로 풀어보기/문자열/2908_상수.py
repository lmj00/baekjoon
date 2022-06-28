num = list(input().split())

for i in range(len(num)):
    l = list(num[i])
    l.reverse()
    num[i] = ''.join(l)

print(num[0] if num[0] > num[1] else num[1])
