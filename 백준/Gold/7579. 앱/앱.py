from sys import stdin

N, M = map(int, stdin.readline().split())
memory = [0] + list(map(int, stdin.readline().split()))
cost = [0] + list(map(int, stdin.readline().split()))

total_cost = sum(cost)

for c in cost:
    total_cost += c

dp = [[0 for j in range(total_cost + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(0, total_cost + 1):
        if j >= cost[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memory[i])
        else:
            dp[i][j] = dp[i - 1][j]


for i in range(0, total_cost + 1):
    if dp[N][i] >= M:
        print(i)
        break
