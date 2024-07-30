from sys import stdin

input = stdin.readline

N = int(input())
moneies = list(map(int, input().split()))
M = int(input())
ans = 0

moneies.sort()

start = 1
end = max(moneies)

while start <= end:
    now_sum = 0
    mid = int((start + end) / 2)

    for money in moneies:
        now_sum += min(mid, money)
    
    if now_sum <= M:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
