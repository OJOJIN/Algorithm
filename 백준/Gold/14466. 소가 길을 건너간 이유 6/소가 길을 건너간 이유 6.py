from sys import stdin
from collections import deque

input = stdin.readline

def cal_direction(r, c):
    if r == -1 and c == 0:
        return 0
    elif r == 0 and c == 1:
        return 1
    elif r == 1 and c == 0:
        return 2
    else:
        return 3
    
def bfs(y, x):
    que = deque()
    que.append((y, x))
    visited[y][x] = True
    cow_cnt = 0
    while que:
        y, x = que.popleft()
        if board[y][x]:
            cow_cnt += 1
        for k in range(4):
            ny = y + direction[k][0]
            nx = x + direction[k][1]
            if 0 < nx <= N and 0 < ny <= N:
                if can_go[y][x][k] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append((ny, nx))
    return cow_cnt
    
N, K, R = map(int, input().split())

board = [[False for _ in range(N+1)] for i in range(N+1)]
# 위 오 아 왼
can_go = [[[True, True, True, True] for i in range(101)] for j in range(101)]
visited = [[False for i in range(N+1)] for j in range(N+1)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cow_cluster = []
ans = 0

for i in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    can_go[r1][c1][cal_direction(r2-r1, c2-c1)] = False
    can_go[r2][c2][cal_direction(r1-r2, c1-c2)] = False

for i in range(K):
    r, c = map(int, input().split())
    board[r][c] = True

for i in range(1, N+1):
    for j in range(1, N+1):
        if not visited[i][j]:
            cow_cluster.append(bfs(i, j))
            
for i in range(len(cow_cluster)):
    for j in range(i + 1, len(cow_cluster)):
        ans += cow_cluster[i] * cow_cluster[j]

print(ans)
