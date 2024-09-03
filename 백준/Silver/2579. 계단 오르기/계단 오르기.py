from sys import stdin

input = stdin.readline

N = int(input())
dp = [[0, 0] for i in range(N+2)]

stair = [int(input()) for _ in range(N)]

for i in range(N):
    if i < N:
        dp[i+1][0] = max(dp[i+1][0], dp[i][1] + stair[i])
        dp[i+2][1] = max(dp[i+2][1], dp[i][0] + stair[i])
        dp[i+2][1] = max(dp[i+2][1], dp[i][1] + stair[i])

print(max(dp[N-1][0], dp[N-1][1]) + stair[N-1])
