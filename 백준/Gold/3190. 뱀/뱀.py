from sys import stdin
from collections import deque

T = 1
F = 1

def move_snake(x, y, forward):
    if forward == 0:
        y -= 1
    elif forward == 1:
        x += 1
    elif forward == 2:
        y += 1
    elif forward == 3:
        x -= 1
    return (x, y)

def turn_head(turn, forward):
    if turn == "D":
        forward = (forward + 1) % 4
    else:
        forward = (forward + 3) % 4
    return forward

N = int(stdin.readline())
K = int(stdin.readline())
snake = deque()
board = [[0 for i in range(N)] for _ in range(N)]
turn_location = ["" for i in range(10001)]

for i in range(K):
    y, x = map(int, stdin.readline().split())
    board[y -1][x - 1] = 1

L = int(stdin.readline())

for i in range(L):
    n, m = map(str, stdin.readline().split())
    turn_location[int(n)] = m

head = (0, 0)
snake.append((0,0))

for i in range(1, 10001):
    head = move_snake(head[0], head[1], F)
    if head in snake or head[0] >= N or head[0] < 0 or head[1] >= N or head[1] < 0:
        print(i)
        break
    if board[head[1]][head[0]] == 1:
        board[head[1]][head[0]] = 0
    else:
        snake.popleft()    
    snake.append(head)

    if turn_location[i] != "":
        F = turn_head(turn_location[i], F)
    i += 1
