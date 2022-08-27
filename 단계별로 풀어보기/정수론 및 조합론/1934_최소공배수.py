import math
import sys

for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gcd = math.gcd(a, b)
    print((a // gcd * b // gcd) * gcd)