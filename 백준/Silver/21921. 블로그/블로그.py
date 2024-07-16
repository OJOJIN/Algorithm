from sys import stdin

input = stdin.readline

N, X = map(int, input().split())

visitor = list(map(int, input().split()))

now_sum = 0
cnt = 1

for i in range(X):
    now_sum += visitor[i]

max_visitors = now_sum

for i in range(X, N):
    now_sum -= visitor[i-X]
    now_sum += visitor[i]
    if now_sum > max_visitors:
        max_visitors = now_sum
        cnt = 1
    elif now_sum == max_visitors:
        cnt += 1

if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(cnt)
