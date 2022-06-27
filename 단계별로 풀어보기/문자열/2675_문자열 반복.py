num = int(input())

for i in range(num):
    s = input()
    count = int(s.split()[0])
    repeat_s = s.split()[1]

    for j in range(len(repeat_s)):
        for k in range(count):
            print(repeat_s[j], end='')
    print()
