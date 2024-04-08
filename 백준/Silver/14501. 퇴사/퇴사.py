N = int(input())
dp = [0 for _ in range(N + 1)]
work = []

for i in range(N):
    work.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i+work[i][0], N + 1):
        if dp[j] < work[i][1] + dp[i]:
            dp[j] = work[i][1] + dp[i]

print(dp[N])
