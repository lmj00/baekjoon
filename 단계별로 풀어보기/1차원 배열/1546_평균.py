num = input()
score_list = list(map(int, input().split()))

max_score = max(score_list)
avg = 0

for i in score_list:
    avg += i / max_score

print(avg / len(score_list) * 100)
