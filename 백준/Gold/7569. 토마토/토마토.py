from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())

box = []
zero_cnt = 0

for idx in range(H):
    h_box = []
    for _ in range(N):
        line = list(map(int, stdin.readline().split()))
        for i in line:
            if i == 0:
                zero_cnt += 1
        h_box.append(line)
    
    box.append(h_box)


que = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                que.append((x, y, z, 0))

cnt = 0
ans = -1

while que:
    a, b, z, seq = que.popleft()
    for nx, ny , nz in [(a - 1, b, z), (a + 1, b, z), (a, b - 1, z), (a, b + 1, z), (a, b, z + 1), (a, b, z - 1)]:
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and box[nz][ny][nx] == 0:
            cnt += 1
            if cnt == zero_cnt:
                ans = seq + 1
                break
            box[nz][ny][nx] = 1
            que.append((nx, ny, nz, seq + 1))
            
if zero_cnt == 0:
    ans = 0
                
print(ans)
