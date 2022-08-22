N, M = map(int, input().split())
board = []
answer_list = []

for _ in range(N):
    s = input()
    board.append(list(s))

color = 'B'

for k in range(2):
    if k == 1:
        color = 'W'
    for i in range(N - 7):
        for j in range(M - 7):
            c = j
            r = i
            r_count = 0
            c_count = 0
            answer = 0

            while True:
                if c_count == 8:
                    c_count = 0
                    c = j
                    r += 1
                    r_count += 1

                    if r_count == 8:
                        answer_list.append(answer)
                        break

                if color != board[r][c]:
                    answer += 1

                if c_count != 7:
                    if color == 'B':
                        color = 'W'
                    else:
                        color = 'B'

                c_count += 1
                c += 1

print(min(answer_list))
