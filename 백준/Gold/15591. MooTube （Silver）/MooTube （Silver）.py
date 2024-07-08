from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline
inf = 2000000000

N, Q = map(int, input().split())

board = [[] for _ in range(N+1)]
for i in range(N-1):
    p, q, r = map(int, input().split())
    board[p].append((q, r))
    board[q].append((p, r))

for i in range(Q):
    k, v = map(int, input().split())
    visitied = [False for _ in range(N+1)]
    que = deque()
    cnt = 0

    for j in board[v]:
        que.append(j)
        que.append(j[1])
        visitied[j[0]] = True

    visitied[v] = True

    while que:
        num, weight = que.popleft()
        cur_min = que.popleft()

        cur_min = min(weight, cur_min)

        if cur_min >= k:
            cnt += 1
            for j in board[num]:
                if not visitied[j[0]]:
                    visitied[j[0]] = True
                    que.append(j)
                    que.append(cur_min)
                
    print(cnt)
