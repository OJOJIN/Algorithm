from sys import stdin
from collections import deque

W, H = map(int, stdin.readline().split())
board = []
glass_board = [[99999999999999 for _ in range(W)] for i in range(H)]
board_positon = [[[False, False] for _ in range(W)] for i in range(H)]
C = []
for _ in range(H):
    board.append(stdin.readline().rstrip())

que = deque()

for y in range(H):
    for x in range(W):
        if board[y][x] == "C":
            C.append((y,x,0, True))
            C.append((y,x,0, False))

que.append(C[0])
que.append(C[1])

while que:
    cur = que.pop()
    for ny in [cur[0] - 1, cur[0] + 1]:
        if ny >= 0 and ny < H:
            if board[ny][cur[1]] != "*":
                if cur[3]:
                    if glass_board[ny][cur[1]] > cur[2] + 1:
                        glass_board[ny][cur[1]] = cur[2] + 1
                        board_positon[ny][cur[1]][0] = True
                        board_positon[ny][cur[1]][1] = False
                        que.appendleft((ny, cur[1], cur[2] + 1, False))
                    elif glass_board[ny][cur[1]] == cur[2] + 1 and not board_positon[ny][cur[1]][0]:
                        board_positon[ny][cur[1]][0] = True
                        que.appendleft((ny, cur[1], cur[2] + 1, False))
                elif glass_board[ny][cur[1]] > cur[2]:
                    glass_board[ny][cur[1]] = cur[2]
                    board_positon[ny][cur[1]][1] = False
                    board_positon[ny][cur[1]][0] = True
                    que.appendleft((ny, cur[1], cur[2], False))
                elif glass_board[ny][cur[1]] == cur[2] and not board_positon[ny][cur[1]][0]:
                    board_positon[ny][cur[1]][0] = True
                    que.appendleft((ny, cur[1], cur[2], False))
                

    for nx in [cur[1] - 1, cur[1] + 1]:
        if nx >= 0 and nx < W:
            if board[cur[0]][nx] != "*":
                if not cur[3]:
                    if glass_board[cur[0]][nx] > cur[2] + 1:
                        glass_board[cur[0]][nx] = cur[2] + 1
                        board_positon[cur[0]][nx][1] = True
                        board_positon[cur[0]][nx][0] = False
                        que.appendleft((cur[0], nx, cur[2] + 1, True))
                    elif glass_board[cur[0]][nx] == cur[2] + 1 and not board_positon[cur[0]][nx][1]:
                        board_positon[cur[0]][nx][1] = True
                        que.appendleft((cur[0], nx, cur[2] + 1, True))
                    
                elif glass_board[cur[0]][nx] > cur[2]:
                    glass_board[cur[0]][nx] = cur[2]
                    board_positon[cur[0]][nx][1] = True
                    board_positon[cur[0]][nx][0] = False
                    que.appendleft((cur[0], nx, cur[2], True))
                elif glass_board[cur[0]][nx] == cur[2] and not board_positon[cur[0]][nx][1]:
                    board_positon[cur[0]][nx][1] = True
                    que.appendleft((cur[0], nx, cur[2], True))

print(glass_board[C[2][0]][C[2][1]])

