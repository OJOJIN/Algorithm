from sys import stdin

str1 = list(stdin.readline())
str2 = list(stdin.readline())

str1.insert(0, 0)
str2.insert(0, 0)

dp = [[0 for j in range(len(str2))] for i in range(len(str1))]
cnt = 0
ans = []

for i in range(1 ,len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
y = len(str1) - 2
x = len(str2) - 2

while dp[y][x] != 0:
    if dp[y - 1][x] == dp[y][x]:
        y -= 1
    elif dp[y][x - 1] == dp[y][x]:
        x -= 1
    else:
        ans.append(str1[y])
        y -= 1
        x -= 1
    

print(dp[len(str1) - 2][len(str2) - 2])
ans.reverse()
for i in ans:
    print(i, end = "")