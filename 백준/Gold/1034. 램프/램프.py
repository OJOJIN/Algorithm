from sys import stdin
from collections import Counter

input = stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]
board_counter = [Counter(board[i]) for i in range(N)]
for i in range(N):
    if not '0' in board_counter[i]:
        board_counter[i]['0'] = 0
K = int(input())
ans = 0

for i in range(N):
    if board_counter[i].get('0') <= K and K % 2 == board_counter[i].get('0') % 2:
        cnt = 0
        for j in range(N):
            if board[i] == board[j]:
                cnt += 1
        ans = max(ans, cnt)
        
print(ans)
