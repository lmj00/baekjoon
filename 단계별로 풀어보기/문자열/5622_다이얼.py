word = list(input())
time = 0
num_str = list("ABC DEF GHI JKL MNO PQRS TUV WXYZ".split())

for i in word:
    for j in num_str:
        if i in j:
            time += 3 + num_str.index(j)


print(time)