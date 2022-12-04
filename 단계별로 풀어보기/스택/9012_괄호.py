for _ in range(int(input())):
    ls = []
    s = input()
    for i in s:
        if i == '(':
            ls.append(i)
        else:
            if len(ls) != 0:
                del ls[-1]
            else:
                ls.append(')')
                break

    if len(ls) != 0:
        print("NO")
    else:
        print("YES")