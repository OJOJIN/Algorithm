from sys import stdin

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, stdin.readline().split())
parent = [i for i in range(N+1)]
component = set()


for _ in range(M):
    u, v = map(int, stdin.readline().split())
    union(u, v)

for i in range(1, N+1):
    component.add(find(parent[i]))

print(len(component))
