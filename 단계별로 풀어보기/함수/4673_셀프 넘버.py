def d(input_num):
    i = 1
    some_list = []

    while i <= input_num:
        num = 0
        condition = str(i)

        for j in range(len(condition)):
            num += int(condition[j])

        num += i
        some_list.append(num)

        if i not in some_list:
            print(i)
        i += 1


d(10000)
