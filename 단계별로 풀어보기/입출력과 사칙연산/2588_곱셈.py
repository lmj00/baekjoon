a = int(input())
b = input()
some_list = []
mul = 1
val = 0

for i in range(len(b) - 1, -1, -1):
    some_list.append(a * int(b[i]))

for i in range(len(b) - 1, - 1, -1):
    val += a * int(b[i]) * mul
    mul *= 10

some_list.append(val)

for i in some_list:
    print(i)
