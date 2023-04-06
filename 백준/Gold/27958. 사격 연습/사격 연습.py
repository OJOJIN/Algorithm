from sys import stdin
from collections import deque
import copy

N = int(stdin.readline())
K = int(stdin.readline())

board = []
dmg = []

global ans
ans = 0

def dfs(cnt, score, current_board):
    global ans

    if score > ans:
        ans = score

    if cnt < K:
        for i in range(N):
            for j in range(N):
                if current_board[i][j] > 0:
                    if current_board[i][j] < 10:
                        if current_board[i][j] <= dmg[cnt]:
                            before = []
                            for ny, nx in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                                if 0 <= nx < N and 0 <= ny < N:
                                    if current_board[ny][nx] == 0:
                                        before.append((ny, nx))
                                        current_board[ny][nx] = int(board[i][j] / 4)
                                        board[ny][nx] = int(board[i][j] / 4)
                            s = current_board[i][j]
                            b = board[i][j]
                            board[i][j] = 0
                            current_board[i][j] = 0
                            dfs(cnt + 1, score + b, current_board)
                            for y, x in before:
                                current_board[y][x] = 0
                                board[y][x] = 0
                            current_board[i][j] = s
                            board[i][j] = b
                            break
                        else:
                            current_board[i][j] -= dmg[cnt]
                            dfs(cnt + 1, score, current_board)
                            current_board[i][j] += dmg[cnt]
                            break
                    else:
                        s = current_board[i][j]
                        current_board[i][j] = 0
                        dfs(cnt + 1, score + s, current_board)
                        current_board[i][j] = s
                        break
        

for i in range(N):
    board.append(list(map(int, stdin.readline().split())))

dmg = list(map(int, stdin.readline().split()))

cur_board = copy.deepcopy(board)

dfs(0, 0, cur_board)

print(ans)