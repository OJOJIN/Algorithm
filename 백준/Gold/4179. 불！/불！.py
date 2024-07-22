from sys import stdin
from collections import deque

input = stdin.readline

R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]
fire_place = set()
que = deque()
ans = 1

for i in range(R):
    for j in range(C):
        if board[i][j] == "J":
            que.append((i,j))
        elif board[i][j] == "F":
            fire_place.add((i,j))

while True:
    now_que = []
    now_fire = []
    
    
    for f in fire_place:
        y = f[0]
        x = f[1]
        for ny, nx in (y-1, x), (y+1, x), (y, x-1), (y, x+1):
            if 0 > ny or R <= ny or 0 > nx or C <= nx:
                continue
            if board[ny][nx] == '#' or board[ny][nx] == 'F':
                continue
            board[ny][nx] = 'F'
            now_fire.append((ny, nx))
    while que:
        y, x = que.popleft()
        for ny, nx in (y-1, x), (y+1, x), (y, x-1), (y, x+1):
            if 0 > ny or R <= ny or 0 > nx or C <= nx:
                print(ans)
                exit(0)
            if board[ny][nx] == '#' or board[ny][nx] == 'F' or board[ny][nx] == 'J':
                continue
            board[ny][nx] = 'J'
            now_que.append((ny, nx))

    ans += 1

    que = deque(now_que)
    fire_place = now_fire

    if not now_que:
        print("IMPOSSIBLE")
        exit(0)
