from sys import stdin

input = stdin.readline

def solve():
    diffusion()
    air_condition()

# 확산!
def diffusion():
    next_board = [[0 for i in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                cur_diffusion(i,j,next_board)
    for i in range(R):
        for j in range(C):
            if board[i][j] != -1:
                board[i][j] = next_board[i][j]

def cur_diffusion(y,x,next_board):
    around_sum = 0
    for ny, nx in (y-1, x), (y+1, x), (y, x-1), (y, x+1):
        if 0 <= ny < R and 0 <= nx < C:
            if board[ny][nx] >= 0:
                next_board[ny][nx] += int(board[y][x] / 5)
                around_sum += int(board[y][x] / 5)
    next_board[y][x] += (board[y][x] - around_sum)

# 공기청정기 레츠고
def air_condition():
    is_first = True
    for i in range(R):
        for j in range(C):
            if board[i][j] == -1 and is_first:
                turn_top(i,j)
                is_first = False
            elif board[i][j] == -1 and not is_first:
                turn_down(i,j)

def turn_top(y, x):
    idx = -1
    ny = 0
    nx = 0
    while True:
        idx = (idx + 1) % 4
        ny = y + top_d[idx][0]
        nx = x + top_d[idx][1]
        if 0 <= ny <= y and 0 <= nx < C:
            break
            
    while True:
        if ny + top_d[idx][0] == y and nx + top_d[idx][1] == x:
            board[ny][nx] = 0
            break
        if 0 <= ny + top_d[idx][0] <= y and 0 <= nx + top_d[idx][1] < C:
            board[ny][nx] = board[ny + top_d[idx][0]][nx + top_d[idx][1]]
            ny += top_d[idx][0]
            nx += top_d[idx][1]
        else:
            idx = (idx + 1) % 4

def turn_down(y, x):
    idx = -1
    ny = 0
    nx = 0
    while True:
        idx = (idx + 1) % 4
        ny = y + down_d[idx][0]
        nx = x + down_d[idx][1]
        if y <= ny < R and 0 <= nx < C:
            break

    while True:
        if ny + down_d[idx][0] == y and nx + down_d[idx][1] == x:
            board[ny][nx] = 0
            break
        if y <= ny + down_d[idx][0] < R and 0 <= nx + down_d[idx][1] < C:
            board[ny][nx] = board[ny + down_d[idx][0]][nx + down_d[idx][1]]
            ny = ny + down_d[idx][0]
            nx = nx + down_d[idx][1]
        else:
            idx = (idx + 1) % 4

R, C , T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
top_d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
down_d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
ans = 2

for i in range(T):
    solve()

for i in range(R):
    for j in range(C):
        ans += board[i][j]

print(ans)
