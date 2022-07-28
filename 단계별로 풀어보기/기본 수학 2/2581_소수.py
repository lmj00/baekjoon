M = int(input())
N = int(input())
result = 0
min_prime = 0
check = 0

for i in range(M, N + 1):
    for j in range(2, i + 1):

        if j == i:
            result += i

            if check == 0:
                min_prime = i
                check += 1

        if i % j == 0:
            break

print(-1) if result == 0 else print(result)
if min_prime != 0:
    print(min_prime)