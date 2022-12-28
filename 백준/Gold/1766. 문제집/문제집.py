import heapq
from sys import stdin

N, M = map(int, stdin.readline().split())

priority = [0] * (N + 1)
step = [[] for i in range(N + 1)]
h = []


for i in range(M):
    a, b = map(int, stdin.readline().split())
    step[a].append(b)
    priority[b] += 1

for i in range(1, N + 1):
    if priority[i] == 0:
        h.append(i)

heapq.heapify(h)

while len(h) != 0:
    a = heapq.heappop(h)
    print(a, end=' ')
    for i in step[a]:
        priority[i] -= 1
        if (priority[i] == 0):
            heapq.heappush(h, i)
