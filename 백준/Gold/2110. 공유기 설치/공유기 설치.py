from sys import stdin

input = stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]

house.sort()

start = 1
end = house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    current = house[0]
    cnt = 1
    for i in range(n):
        if current + mid <= house[i]:
            cnt += 1
            current = house[i]
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)