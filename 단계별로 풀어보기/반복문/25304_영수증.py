X = int(input())
price = 0

for i in range(int(input())):
    m, c = map(int, input().split())
    price += m * c

print("Yes") if X == price else print("No")