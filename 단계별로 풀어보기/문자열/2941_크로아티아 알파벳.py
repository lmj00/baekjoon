word = input()
word_len = len(word)

croaita = list("c= c- dz= d- lj nj s= z=".split())
i = 0
count = 0

while i < len(croaita):
    if croaita[i] in word:
        word = word.replace(croaita[i], ' ', 1)
        count += 1
        i = 0
    else:
        i += 1

for j in word:
    if j != '-' and j != '=' and j != ' ':
        count += 1

print(count)
