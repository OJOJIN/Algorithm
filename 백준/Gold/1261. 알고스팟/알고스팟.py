from collections import deque
from sys import stdin


def bfs():
    queue = deque()
    queue.appendleft([1, 1, 0])
    visited[1][1] = 0

    while queue:
        a = queue.pop()

        x = a[0]
        y = a[1]

        for nx in [x - 1, x + 1]:
            if nx > 0 and nx <= n:
                if miro[y][nx] == 0 and visited[y][nx] > visited[y][x]:
                    visited[y][nx] = visited[y][x]
                    queue.appendleft([nx, y])
                elif miro[y][nx] == 1 and visited[y][nx] > visited[y][x] + 1:
                    visited[y][nx] = visited[y][x] + 1
                    queue.appendleft([nx, y])
        for ny in [y - 1, y + 1]:
            if ny > 0 and ny <= m:
                if miro[ny][x] == 0 and visited[ny][x] > visited[y][x]:
                    visited[ny][x] = visited[y][x]
                    queue.appendleft([x, ny])
                elif miro[ny][x] == 1 and visited[ny][x] > visited[y][x] + 1:
                    visited[ny][x] = visited[y][x] + 1
                    queue.appendleft([x, ny])


n, m = map(int, stdin.readline().split())

miro = [[0 for j in range(n + 1)] for i in range(m + 1)]
visited = [[999999 for j in range(n + 1)] for i in range(m + 1)]

for i in range(1, m + 1):
    s = stdin.readline()
    for j in range(1, n + 1):
        miro[i][j] = int(s[j - 1])

bfs()
print(visited[m][n])
