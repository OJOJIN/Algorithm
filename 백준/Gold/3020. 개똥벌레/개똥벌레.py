# 2023.10.30
from sys import stdin

N, H = map(int, stdin.readline().split())
bottom = set()
top = set()
bottom_count = [0 for _ in range(H)]
top_count = [0 for _ in range(H)]

min = 200001
ans = 0

for i in range(N):
    h = int(stdin.readline())
    if i % 2 == 0:
        bottom.add(h)
        bottom_count[h - 1] += 1
    else:
        top.add(h)
        top_count[h - 1] += 1

for i in range(H - 1, 0, -1):
    bottom_count[i - 1] += bottom_count[i]
    top_count[i - 1] += top_count[i]

top_count.reverse()

for i in range(0, H):
    sum = top_count[i] + bottom_count[i]
    if sum < min:
        min = sum
        ans = 1
    elif sum == min:
        ans += 1
print(min, ans)

