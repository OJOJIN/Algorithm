from sys import stdin
from collections import deque
from copy import deepcopy

N, M = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())

def front(y, x, f):
    if f == 0:
        return (y - 1, x)
    elif f == 1:
        return (y, x + 1)
    elif f == 2:
        return (y + 1, x)
    else:
        return (y, x - 1)
    
def back(y, x, f):
    if f == 0:
        return (y + 1, x)
    elif f == 1:
        return (y, x - 1)
    elif f == 2:
        return (y - 1, x)
    else:
        return (y, x + 1)

room = []
ans = 0

for i in range(N):
    room.append(list(map(int, stdin.readline().split())))

cleaned = deepcopy(room)

que = deque()
que.append((r, c, d))

while que:
    y, x, position = que.popleft()
    
    if cleaned[y][x] == 0:
        cleaned[y][x] = 1
        ans += 1
    
    remain = False

    for ny, nx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        if 0 <= ny < N and 0 <= nx < M:
            if cleaned[ny][nx] == 0:
                remain = True
                break
    
    if remain == True:
        position = (position + 3) % 4
        ny, nx = front(y, x, position)
        if cleaned[ny][nx] == 0:
            que.append((ny, nx, position))
        else:
            que.append((y, x, position))
    else:
        ny, nx = back(y, x, position)
        if room[ny][nx] == 0:
            que.append((ny, nx, position))
        else:
            break

print(ans)