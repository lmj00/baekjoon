N, K = map(int, input().split())
temp = list(map(int, input().split()))
sum_list = []

for j in range(len(temp) - 1):
    temp[j + 1] += temp[j]
temp.insert(0, 0)

for i in range(K, len(temp)):
    sum_list.append(temp[i] - temp[i - K])
print(max(sum_list))