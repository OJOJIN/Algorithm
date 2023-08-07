from sys import stdin
from collections import deque
from copy import deepcopy

N, M = map(int, stdin.readline().split())
board = []
virus = []
virus_location = []
ans = 64
wall = 0

for _ in range(N):
    board.append(list(map(int, stdin.readline().split())))

# 바이러스 위치 받기
for i in range(N):
    for j in range(M):
        # 바이러스 체크
        if board[i][j] == 2:
            virus.append([i, j])
            virus_location.append(i*M + j)
        # 벽 개수 세기(정답 구할 때 전체칸 - 벽 - 바이러스 로 구할거)
        if board[i][j] == 1:
            wall += 1



# O(n) = N*M ^ 3 (64 ^ 3 = 262,144) 
# a, b, c 위치에 벽을 세워버릴거임
for a in range(N * M):
    
    # 해당 위치가 빈칸(0)이 아니면 continue
    if not board[int(a/M)][a%M] == 0:
        continue
    for b in range(a + 1, N * M):
        if not board[int(b/M)][b%M] == 0:
            continue
        for c in range(b + 1, N * M):
            if not board[int(c/M)][c%M] == 0:
                continue
            curBoard = deepcopy(board)
            
            # 벽 세우기 코드
            for i in (a, b, c):
                y = int(i / M)
                x = i % M
                curBoard[y][x] = 1
            
            que = deque()
            cnt = 0
            # 바이러스 위치 que에 담기
            for v in virus:
                que.append(v)

            # BFS 활용해서 바이러스 퍼트리기
            while que:
                # cnt 변수 활용해서 바이러스 개수 세기
                cnt += 1

                cur = que.pop()
                for ny, nx in ((cur[0] + 1, cur[1]), (cur[0] - 1, cur[1]), (cur[0], cur[1] + 1), (cur[0], cur[1] - 1)):

                    # 연구실 크기 밖으로 안넘어가게 확인 (OutOfBound 막기)
                    if nx >= 0 and nx < M and ny >= 0 and ny < N:
                        # 빈 곳이면 들어가기
                        if curBoard[ny][nx] == 0:
                            curBoard[ny][nx] = 2
                            que.append([ny, nx])
            
            if ans > cnt:
                ans = cnt

print(N*M-ans-wall-3)
