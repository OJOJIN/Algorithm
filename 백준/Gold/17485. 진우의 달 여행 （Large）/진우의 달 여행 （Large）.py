from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
INF = 99999999

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[INF, INF, INF]for _ in range(M)] for i in range(N)]

for i in range(M):
    for j in range(3):
        dp[0][i][j] = board[0][i]

for i in range(N-1):
    for j in range(M):
        for nx in [j-1, j, j+1]:
            if 0 <= nx < M:
                d = nx - j + 1 
                for nd in range(3):
                    if d == nd:
                        continue
                    dp[i+1][j][d] = min(dp[i][nx][nd] + board[i+1][j], dp[i+1][j][d])

ans = INF

for i in dp[N-1]:
    for j in i:
        ans = min(ans, j)

print(ans)
