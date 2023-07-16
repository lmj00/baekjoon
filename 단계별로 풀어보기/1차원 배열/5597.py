a = [int(input()) for i in range(28)]
b = [j + 1 for j in range(30)]

print(*sorted(set(b) - set(a)), sep='\n')