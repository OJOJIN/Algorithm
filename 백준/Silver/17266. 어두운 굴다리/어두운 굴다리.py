from sys import stdin
from math import ceil

input = stdin.readline

N = int(input())
M = int(input())
line = list(map(int, input().split()))

line.sort()
before = 0
ans = 0
for now in line:
    ans = max(ans, now - before)
    before = now

ans = max(ans, 2*(line[0] - 0))
ans = max(ans, 2*(N - line[M-1]))

print(ceil(ans/2))
