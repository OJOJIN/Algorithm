from sys import stdin

def find(n):
    if n == parent[n]:
        return n
    else:
        parent[n] = find(parent[n])
        return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[a] = b

N = int(stdin.readline())
M = int(stdin.readline())
parent = [i for i in range(N + 1)]

for i in range(1, N + 1):
    can_go = list(map(int, stdin.readline().split()))
    for j in range(1, N + 1):
        if can_go[j - 1] == 1:
            union(i, j)

want_go = list(map(int, stdin.readline().split()))

for i in range(len(want_go) - 1):
    if find(want_go[i]) != find(want_go[i + 1]):
        print("NO")
        exit(0)

print("YES")
