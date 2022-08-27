s = input()
test = {}

for i in range(len(s)):
    k = 0
    for j in range(i, len(s)):
        test[s[k:j + 1]] = ''
        k += 1
print(len(test))