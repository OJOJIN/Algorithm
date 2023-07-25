from sys import stdin
import sys

sys.setrecursionlimit(10**5)

def find(x):
    if gate[x] == x:
        return x
    gate[x] = find(gate[x])
    return gate[x]

G = int(stdin.readline())
P = int(stdin.readline())
gate = [i for i in range(G + 1)]
ans = 0

for _ in range(P):
    cur = int(stdin.readline())
    gate[find(cur)] -= 1
    if gate[gate[cur]] < 0:
        break
    ans += 1

print(ans)