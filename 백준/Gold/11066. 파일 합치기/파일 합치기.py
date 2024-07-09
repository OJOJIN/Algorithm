from sys import stdin

input = stdin.readline
INF = 9999999999999

def solve():
    K = int(input())
    dp = [list(map(int, input().split()))]
    for i in range(K-1):
        dp.append([INF] * (K-i-1))

    dp_sum = [[0 for _ in range(K)]]
    for i in range(K-1):
        dp_sum.append([INF] * (K-i-1))

    for i in range(1, K):
        for j in range(K-i):
            for k in range(i):
                if dp_sum[i][j] > dp[i-k-1][j] + dp[k][j+i-k] + dp_sum[i-k-1][j] + dp_sum[k][j+i-k]:
                    dp[i][j] = dp[i-k-1][j] + dp[k][j+i-k]
                    dp_sum[i][j] = dp[i-k-1][j] + dp[k][j+i-k] + dp_sum[i-k-1][j] + dp_sum[k][j+i-k]
    print(dp_sum[K-1][0])

T = int(input())

while T > 0:
    T -= 1
    solve()
