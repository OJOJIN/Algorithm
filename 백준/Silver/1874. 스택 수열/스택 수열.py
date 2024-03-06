from sys import stdin
from collections import deque

N = int(stdin.readline())

num = 1
que = deque()
ans = []

for i in range(N):
    n = int(stdin.readline())
    if n >= num:
        for j in range(num, n+1):
            que.append(j)
            ans.append('+')
        num = n + 1
    pop_num = que.pop()
    ans.append('-')
    if pop_num != n:
        print('NO')
        exit(0)

for i in ans:
    print(i)