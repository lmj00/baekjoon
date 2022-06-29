a, b, c = map(int, input().split())
print(-1) if c - b <= 0 else print((a + (c - b)) // (c - b))
