from sys import stdin
import heapq

input = stdin.readline
INF = 9999999999
V, E = map(int, input().split())
start = int(input())
board = [[] for i in range(V + 1)]
ans_list = [INF for i in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    board[u].append((v, w))

ans_list[start] = 0
heap_list = []

for i in board[start]:
    heapq.heappush(heap_list, [i[1], i[0]])
    ans_list[i[0]] = min(ans_list[i[0]], i[1])

while heap_list:
    now_weight, now_node = heapq.heappop(heap_list)
    if ans_list[now_node] < now_weight:
        continue
    for i in board[now_node]:
        if ans_list[i[0]] > now_weight + i[1]:
            ans_list[i[0]] = now_weight + i[1]
            heapq.heappush(heap_list, [ans_list[i[0]], i[0]])

for i in ans_list[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)
