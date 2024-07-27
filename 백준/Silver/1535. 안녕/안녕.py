from sys import stdin

input = stdin.readline

N = int(input())
L = [0] + list(map(int, input().split()))
H = [0] + list(map(int, input().split()))
dp = [[0 for i in range(100)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1, 100):
        if j >= L[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + H[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])
