def find():
    num = int(input())
    count = 0
    final_count = 0

    for i in range(1, num + 1):
        str_list = [j for j in str(i)]

        if i < 100:
            final_count += 1
            continue
        else:
            pivot = int(str_list[1]) - int(str_list[0])

        for k in range(len(str_list) - 1):
            if int(str_list[k]) + pivot == int(str_list[k + 1]):
                count += 1

        if count == len(str_list) - 1:
            final_count += 1

        count = 0
        str_list.clear()

    return final_count

print(find())
