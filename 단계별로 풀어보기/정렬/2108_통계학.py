import decimal
import sys
from collections import Counter

n = int(sys.stdin.readline())
s_list = [(int(sys.stdin.readline())) for i in range(n)]

s_list.sort()
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
cnt = Counter(s_list).most_common(2)

if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    cnt = cnt[1][0]
else:
    cnt = cnt[0][0]

print(round(sum(s_list) / n))
print(s_list[len(s_list) // 2])
print(cnt)
print(s_list[-1] - s_list[0])