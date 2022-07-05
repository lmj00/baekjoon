count = int(input())

for i in range(count):
    h, w, n = map(int, input().split())
    room = 1

    while True:
        if h >= n:
            if room < 10:
                print(f"{n}0{room}")
            else:
                print(f"{n}{room}")
            break

        n -= h
        room += 1
