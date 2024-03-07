from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10**4)

is_grouping = False

def dfs(y, x, num):
    global is_grouping
    if board_group[y][x] == 0:
        board_group[y][x] = num
        group[num].append((y,x))
    for ny, nx in (y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1):
        if ny >= 0 and ny < N and nx >= 0 and nx < N and board_group[ny][nx] == 0:
            diff = abs(board[y][x] - board[ny][nx])
            if L <= diff and diff <= R:
                group[num].append((ny, nx))
                board_group[ny][nx] = num
                dfs(ny, nx, num)
                is_grouping = True

N, L , R = map(int, stdin.readline().split())

board = []
ans = 0

for i in range(N):
    board.append(list(map(int, stdin.readline().split())))

while(1):
    is_grouping = False
    board_group = [[0 for i in range(N)] for j in range(N)]
    group = [[] for _ in range(N * N + 1)]
    n = 1
    for i in range(N):
        for j in range(N):
            dfs(i, j, n)
            n += 1
    if not is_grouping:
        print(ans)
        exit(0)
    for i in range(N * N + 1):
        sum = 0
        for j in group[i]:
            sum += board[j[0]][j[1]]
        for j in group[i]:
            board[j[0]][j[1]] = int(sum / len(group[i]))

    ans += 1
