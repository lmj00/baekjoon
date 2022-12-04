ls = [int(input()) for _ in range(5)]
ls.sort()

print(sum(ls) // 5)
print(ls[2])

'''
import statistics

ls = [int(input()) for _ in range(5)]
mean = statistics.mean(ls)
ls.sort()

print(mean)
print(ls[len(ls) // 2])
'''