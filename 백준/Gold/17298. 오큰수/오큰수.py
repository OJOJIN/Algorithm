from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
heap = []
ans = [-1 for _ in range(N)]

for i in range(0, N):
    heappush(heap, (arr[i], i))
    while arr[i] > heap[0][0]:
        ans[heap[0][1]] = arr[i]
        heappop(heap)    

print(*ans)
