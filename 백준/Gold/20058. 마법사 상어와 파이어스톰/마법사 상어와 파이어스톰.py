import copy
import sys

sys.setrecursionlimit(100000)

def fire_storm(l):
    for y in range(0, 2**N, 2**l):
        for x in range(0, 2**N, 2**l):
            for i in range((2**l)):
                for j in range((2**l)):
                    change_board[i+x][j+y] = board[(2**l)-1-j+x][i+y]

def check_melt_all_board():
    for i in range(2**N):
        for j in range(2**N):
            if board[i][j] > 0:
                change_board[i][j] = melt_ice(i, j)

def melt_ice(y, x):
    cnt = 0
    for ny, nx in (y+1, x), (y-1, x), (y, x-1), (y, x+1):
        if 0 <= nx < 2**N and 0 <= ny < 2**N:
            if board[ny][nx] > 0:
                cnt += 1
    if cnt >= 3:
        return board[y][x]
    else:
        return board[y][x] - 1

def dfs(y, x):
    global size_cur

    visited[y][x] = True

    for ny, nx in (y+1, x), (y-1, x), (y, x-1), (y, x+1):
        if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
            if board[ny][nx] > 0 and not visited[ny][nx]:
                size_cur += 1
                dfs(ny, nx)

N, Q = map(int, input().split())


board = []
change_board = [[0 for _ in range(2**N)] for i in range(2**N)]
visited = [[False for _ in range(2**N)] for i in range(2**N)]

size_cur = 0
size_ans = 0

for _ in range(2**N):
    board.append(list(map(int, input().split())))

L = list(map(int, input().split()))

for l in range(Q):
    fire_storm(L[l])
    board = copy.deepcopy(change_board)
    check_melt_all_board()
    board = copy.deepcopy(change_board)

sum = 0

for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j] and board[i][j] > 0:
            size_cur = 0
            dfs(i, j)
            size_ans = max(size_ans, size_cur + 1)
        sum += board[i][j]

print(sum)
print(size_ans)