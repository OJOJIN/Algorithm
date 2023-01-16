from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())

box = []
zero_cnt = 0

for _ in range(N):
    line = list(map(int, stdin.readline().split()))
    for i in line:
        if i == 0:
            zero_cnt += 1
    box.append(line)


que = deque()

for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            que.append((x, y, 0))

cnt = 0
ans = -1

while que:
    a, b, seq = que.popleft()
    for nx, ny in [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]:
        if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
            cnt += 1
            if cnt == zero_cnt:
                ans = seq + 1
                break
            box[ny][nx] = 1
            que.append((nx, ny, seq + 1))
            
if zero_cnt == 0:
    ans = 0
                
print(ans)
