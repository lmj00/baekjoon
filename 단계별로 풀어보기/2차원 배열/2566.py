a = [list(map(int, input().split())) for _ in range(9)]
max_v = 0

for v in a:
    max_v = max(*v, max_v)

for i, v in enumerate(a):
    if max_v in [*v]:
        print(max_v)
        print(i + 1, [*v].index(max_v) + 1)
        break