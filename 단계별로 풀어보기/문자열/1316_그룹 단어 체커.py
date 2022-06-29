num = int(input())
word_list = [(input()) for i in range(num)]
check_list = []
count = 0
answer = 0

for i in word_list:
    check_list.append(i[0])
    count += 1
    for j in range(1, len(i)):
        if check_list[-1] != i[j]:
            if i[j] not in check_list:
                check_list.append(i[j])
                count += 1
            else:
                break
        else:
            count += 1

    if count == len(i):
        answer += 1

    count = 0
    check_list.clear()

print(answer)
