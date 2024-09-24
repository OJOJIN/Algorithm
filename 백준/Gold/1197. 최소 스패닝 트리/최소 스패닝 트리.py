from sys import stdin

input = stdin.readline

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    p1 = find(a)
    p2 = find(b)

    if p1 < p2:
        parents[p2] = p1
    else:
        parents[p1] = p2

V, E = map(int, input().split())
parents = [i for i in range(V+1)]
edges = [list(map(int, input().split())) for _ in range(E)]
ans = 0
cnt = 0

edges.sort(key = lambda x: x[2])

for a, b, w in edges:
    if find(a) != find(b):
        union(a, b)
        ans += w
        cnt += 1
    if cnt == V - 1:
        break

print(ans)
