from collections import deque

def bfs(y, x):
    cnt = 1
    que = deque()
    que.append((y, x))
    while que:
        y, x = que.popleft()
        visited[y][x] = True
        for ny, nx in (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1):
            if ny < 0 or N <= ny or nx < 0 or N <= nx:
                continue
            if visited[ny][nx]:
                continue
            if board[ny][nx] == 0:
                continue
            visited[ny][nx] = True
            que.append((ny, nx))
            cnt += 1

    return cnt

N = int(input())
board = []
visited = [[False for i in range(N)] for _ in range(N)]
danji_cnt = []

for i in range(N):
    line = input()
    board.append([int(n) for n in line])

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            danji_cnt.append(bfs(i, j))

print(len(danji_cnt))
danji_cnt.sort()
for cnt in danji_cnt:
    print(cnt)
            