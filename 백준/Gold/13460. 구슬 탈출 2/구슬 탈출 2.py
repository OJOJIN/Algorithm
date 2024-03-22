import sys
sys.setrecursionlimit(2000000)

def move_back(y, x, d):
    if d == 0:
        y += 1
    elif d == 1:
        x -= 1
    elif d == 2:
        y -= 1
    else:
        x += 1
    return (y, x)

def move_front(y, x, d):
    if d == 0:
        y -= 1
    elif d == 1:
        x += 1
    elif d == 2:
        y += 1
    else:
        x -= 1
    return (y, x)

def check_blue(b):
    if board[b[0]][b[1]] == 'O':
        return True
            
def check_red(r, cnt):
    global ans
    if board[r[0]][r[1]] == 'O':
        ans = min(ans, cnt)
      
def move_ball(y, x, d):
    if d == 0:
        while 1:
            if board[y-1][x] != '.':
                break
            y -= 1
    elif d == 1:
        while 1:
            if board[y][x+1] != '.':
                break
            x += 1
    elif d == 2:
        while 1:
            if board[y+1][x] != '.':
                break
            y += 1
    else:
        while 1:
            if board[y][x-1] != '.':
                break
            x -= 1
    return (y, x)

def is_red_front(r, b, d):
    if d == 0:
        return r[0] < b[0]
    elif d == 1:
        return r[1] > b[1]
    elif d == 2:
        return r[0] > b[0]
    else:
        return r[1] < b[1]

def dfs(cnt, r, b):
    if cnt == 11:
        return
    for i in range(4):
        original_r = r
        original_b = b
        b = move_ball(b[0], b[1], i)
        if check_blue(move_front(b[0], b[1], i)):
            r = original_r
            b = original_b
            continue
        r = move_ball(r[0], r[1], i)
        check_red(move_front(r[0], r[1], i), cnt)
        if r == b:
            if is_red_front(original_r, original_b, i):
                b = move_back(b[0], b[1], i)
            else:
                r = move_back(r[0], r[1], i)
        dfs(cnt+1, r, b)
        r = original_r
        b = original_b

ans = 11
input = sys.stdin.readline
A = 1
N, M = map(int, input().split())
board = []
r_position = (0, 0)
b_position = (0, 0)

for i in range(N):
    board.append(list(input().rstrip()))

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            board[i][j]='.'
            r_position = (i, j)
        elif board[i][j] == "B":
            board[i][j]='.'
            b_position = (i, j)

dfs(1, r_position, b_position)
if ans == 11:
    print(-1)
else:
    print(ans)
