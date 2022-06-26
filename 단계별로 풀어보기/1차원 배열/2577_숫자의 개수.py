nums = [input() for i in range(3)]

result = str(eval("*".join([i for i in nums])))

for i in range(10):
    print(result.count(str(i)))
