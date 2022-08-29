import math

for i in range(int(input())):
    N, K = map(int, input().split())
    max_v = max(N, K)
    min_v = min(N, K)
    print(math.comb(max_v, min_v))