from sys import stdin
import sys

sys.setrecursionlimit(300000)

def find(n):
    if n == parent[n]:
        return n
    else:
        parent[n] = find(parent[n])
        return parent[n]

def union(a, b):
    a_top = find(a)
    b_top = find(b)

    if a_top != b_top:
        parent[a_top] = b

N = int(stdin.readline())

parent = [i for i in range(N + 1)]

for _ in range(N - 2):
    a, b = map(int, stdin.readline().split())
    union(a,b)
for i in range(2, N + 1):
    if find(1) != find(i):
        print(1, i)
        exit(0)