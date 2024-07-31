from sys import stdin
import heapq

input = stdin.readline

def dijkstra(st):
    q = []
    heapq.heappush(q, (0, st))
    while q:
        w, now = heapq.heappop(q)
        if distance[st][now] < w:
            continue
        for d, t in road[now]:
            if distance[st][d] > w + t:
                distance[st][d] = w + t
                heapq.heappush(q, (w + t, d))


N, M, X = map(int, input().split())
road = [[] for _ in range(N+1)]
distance = [[10000001 for _ in range(N+1)] for i in range(N+1)]
ans = 0

for i in range(M):
    a, b, t = map(int, input().split())
    road[a].append((b, t))

for i in range(1, N+1):
    if i == X:
        continue
    dijkstra(i)

dijkstra(X)

for i in range(1, N+1):
    if i == X:
        continue
    ans = max(ans, distance[i][X] + distance[X][i])

print(ans)
