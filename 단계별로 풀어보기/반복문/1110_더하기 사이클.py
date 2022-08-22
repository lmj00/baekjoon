a = input()
count = 0

if int(a) < 10:
    a = "0" + a

b = a[1] + str(int(a[0]) + int(a[1]))[-1]
count += 1

while a != b:
    count += 1
    b = b[1] + str(int(b[0]) + int(b[1]))[-1]

print(count)
