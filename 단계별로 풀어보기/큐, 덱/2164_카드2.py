from collections import deque
dq = deque(i + 1 for i in range(int(input())))
copy_dq = dq.copy()

for i in range(len(dq) - 1):
    copy_dq.popleft()
    v = copy_dq.popleft()
    copy_dq.append(v)

print(copy_dq[0])