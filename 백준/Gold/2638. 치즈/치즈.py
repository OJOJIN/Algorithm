import sys
sys.setrecursionlimit(10001)

def dfs_air(y, x):
    air[y][x] = True
    for ny, nx in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
        if ny >= 0 and ny < N and nx >= 0 and nx < M:
            if not air[ny][nx] and board[ny][nx] == 0:
                dfs_air(ny, nx)

def check_around(y, x):
    cnt = 0
    for ny, nx in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
        if air[ny][nx]:
            cnt += 1
    return cnt >= 2

input = sys.stdin.readline

N, M = map(int, input().split())

ans = 0
board = []
air = [[False for _ in range(M)] for i in range(N)]

for i in range(N):
    board.append(list(map(int, input().split())))

dfs_air(0, 0)

while 1:

    new_air = []

    is_cheese = False
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and check_around(i, j):
                board[i][j] = 0
                new_air.append((i, j))

    for i in new_air:
        air[i[0]][i[1]] = True
        dfs_air(i[0], i[1])

    if not new_air:
        break
    ans += 1

print(ans)
