from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())

before = [0] * (n + 1)
front = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, stdin.readline().split())
    front[a].append(b)
    before[b] += 1

que = deque()

for i in range(1, n + 1):
    if before[i] == 0:
        que.append(i)

while que:
    a = que.popleft()
    print(a, end=" ")

    for i in front[a]:
        before[i] -= 1
        if before[i] == 0:
            que.append(i)
