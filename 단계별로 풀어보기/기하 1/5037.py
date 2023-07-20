from collections import Counter

while True:
    ls = list(map(int, input().split()))
    ls.sort()
    c = Counter(ls).most_common()

    if sum(ls) == 0:
        break
    if len(c) == 1:
        print('Equilateral')
    elif ls[0] + ls[1] > ls[2]:
        if len(c) == 2:
            print('Isosceles')
        elif len(c) == 3:
            print('Scalene')
    else:
        print('Invalid')