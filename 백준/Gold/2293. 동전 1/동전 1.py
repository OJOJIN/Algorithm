from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
coins = set()
dp = [0] * (k+1)
dp[0] = 1

for i in range(n):
    coins.add(int(input()))

for c in coins:
    for i in range(c, k+1):
        dp[i] += dp[i-c]

print(dp[k])
