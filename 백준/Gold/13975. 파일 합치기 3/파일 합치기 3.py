from sys import stdin
from heapq import heappop, heappush

T = int(input())

while T > 0:
    T -= 1
    ans = 0
    heap = []

    N = int(input())
    files = list(map(int, stdin.readline().split()))
    for file in files:
        heappush(heap, file)
    
    while len(heap) > 1:
        n1 = heappop(heap)
        n2 = heappop(heap)
        ans += (n1 + n2)
        heappush(heap, n1 + n2)

    print(ans)
    