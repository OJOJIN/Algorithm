from sys import stdin
from sys import stdout
from collections import deque

n, m = map(int, stdin.readline().split())

total = n * m

map = []
can_move = [[True for j in range(m + 1)] for i in range(n + 1)]
can_move_group = [[-1 for j in range(m + 1)] for i in range(n + 1)]
group_high = [0 for _ in range(total + 1)]
ans = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    a = list(stdin.readline())
    b = []
    for j in a:
        if not j == '\n':
            b.append(int(j))
    map.append(b)

que = deque()
t = 0

for num in range(total):
    x = num % m
    y = int(num / m)   

    if map[y][x] == 0 and can_move[y][x]:
        t += 1
        cnt = 1
        que.append((x, y))

        while que:
            x, y = que.popleft()
            can_move_group[y][x] = num
            can_move[y][x] = False

            for nx, ny in ([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]):
                if 0 <= nx < m and 0 <= ny < n and map[ny][nx] == 0 and can_move[ny][nx]:
                    can_move[ny][nx] = False
                    cnt += 1
                    que.append((nx, ny))
            
        group_high[num] = cnt


for num in range(total):
    x = num % m
    y = int(num / m)
    group = set()
    if map[y][x] == 1:
        move = 1
        for nx, ny in ([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]):
            if 0 <= nx < m and 0 <= ny < n and not can_move_group[ny][nx] in group:
                group.add(can_move_group[ny][nx])
                move += group_high[can_move_group[ny][nx]]

        ans[y][x] = move

for i in ans:
    for j in i:
        stdout.write("%d" % (j % 10))
    stdout.write("\n")