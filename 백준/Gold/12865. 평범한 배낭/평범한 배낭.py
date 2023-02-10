from sys import stdin

n, k = map(int, stdin.readline().split())
dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
m = [0] + []

for i in range(1, n + 1):   
    w, v = map(int, stdin.readline().split())
    m.append([w,v])

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= m[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - m[i][0]] + m[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])