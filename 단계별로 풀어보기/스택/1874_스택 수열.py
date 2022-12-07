from collections import deque
import sys

stack = deque()
N = int(input())
seq = deque(int(sys.stdin.readline()) for _ in range(N))

j = 0
answer = []
val = seq.popleft()

for i in range(1, N + 1):
    stack.append(i)
    answer.append('+')

    while len(stack) != 0 and stack[j] == val:
        stack.pop()
        if len(seq) != 0:
            val = seq.popleft()
        answer.append('-')

        j -= 1
    j += 1

if len(stack) > 0:
    print("NO")
else:
    [print(i) for i in answer]