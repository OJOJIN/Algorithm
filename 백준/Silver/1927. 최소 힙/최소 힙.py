import heapq
from sys import stdin

input = stdin.readline

N = int(input())

heap_list = []

for i in range(N):
    n = int(input())
    if n == 0:
        if heap_list:
            print(heapq.heappop(heap_list))
        else:
            print(0)
    else:
        heapq.heappush(heap_list, n)
