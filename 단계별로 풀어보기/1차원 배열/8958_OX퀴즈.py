num = int(input())

for i in range(num):
    case = input()
    count = 0
    for j in range(len(case)):
        if case[j] == "O":
            count += 1

            while j + 1 < len(case):
                if case[j + 1] == "O":
                    count += 1
                    j += 1
                else:
                    break
    print(count)


''' 
num = int(input())

case_list = [input() for i in range(num)]

for i in range(len(case_list)):
    count = 0
    for j in range(len(case_list[i])):
        if case_list[i][j] == "O":
            count += 1

            while j + 1 < len(case_list[i]):
                if case_list[i][j + 1] == "O":
                    count += 1
                    j += 1
                else:
                    break
    print(count)
'''