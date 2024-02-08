from sys import stdin
from collections import deque

N = int(stdin.readline())
M = list(map(int,  stdin.readline().split()))
M.reverse()

que = deque()
one = 0

for i in range(N):
    if M[i] == 1:
        if one != 0:
            que.appendleft(one)
        one = i + 1
    elif M[i] == 2:
        que.appendleft(i + 1)
    else:
        que.append(i + 1)
que.appendleft(one)

print(*que)