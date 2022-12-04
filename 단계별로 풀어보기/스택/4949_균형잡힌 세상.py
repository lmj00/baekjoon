import sys

while True:
    s = sys.stdin.readline()
    ls = []

    if s[0] == '.':
        break

    for i in s:
        if i == '(' or i == '[':
            ls.append(i)

        if i == ')' or i == ']':
            if len(ls) != 0:
                if ls[-1] == '(' and i == ')' or ls[-1] == '[' and i == ']':
                    del ls[-1]
                else:
                    ls.append('')
                    break
            else:
                ls.append('')
                break

    if len(ls) == 0:
        print("yes")
    else:
        print("no")
