from fractions import Fraction

N = int(input())
s_list = list(map(int, input().split()))

for i in range(1, N):
    f = Fraction(s_list[i], s_list[0])
    print(f"{f.denominator}/{f.numerator}")