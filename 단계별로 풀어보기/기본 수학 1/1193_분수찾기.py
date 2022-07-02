num = int(input())

count = 0
i = 1

while i < num + 1:
    count += 1
    i += count

if count % 2 == 0:
    print(f"{count - i + num + 1}/{i - num}")
else:
    print(f"{i - num}/{count - i + num + 1}")
