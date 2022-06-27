num = int(input())

for i in range(num):
    score_list = list(map(int, input().split()))
    score_count = score_list[0]
    del(score_list[0])
    avg = sum(score_list) / score_count

    avg_per = 0
    for j in score_list:
        if j > avg:
            avg_per += 1

    print(f"{round(avg_per / score_count * 100, 3):.3f}%")
