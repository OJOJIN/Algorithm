from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**4)

input = stdin.readline


def dfs(y, x):
    for ny, nx in (y-1, x), (y-1, x+1), (y, x+1), (y+1, x+1), (y+1, x), (y+1, x-1), (y, x-1), (y-1, x-1):
        if ny < 0 or H <= ny or nx < 0 or W <= nx:
            continue
        if board[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx)

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    board = [list(map(int, input().split())) for _ in range(H)]
    visited = [[False for _ in range(W)] for i in range(H)]
    cnt = 0

    for i in range(H):
        for j in range(W):
            if board[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                cnt += 1
    print(cnt)
