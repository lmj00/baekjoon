from collections import Counter

ls = [int(input()) for i in range(3)]
c = Counter(ls).most_common()

if ls[0] == ls[1] == ls[2] == 60:
    print('Equilateral')
elif sum(ls) == 180 and len(c) == 2:
    print('Isosceles')
elif sum(ls) == 180 and len(c) == 3:
    print('Scalene')
else:
    print('Error')