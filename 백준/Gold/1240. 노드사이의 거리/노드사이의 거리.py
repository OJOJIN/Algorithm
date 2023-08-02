from sys import stdin

global ans

def dfs(a, target, cnt):
    if a == target:
        print(cnt)
        return
    for next in can_go[a]:
        if not is_in[next]:
            is_in[next] = True
            dfs(next, target, cnt + node[a][next])
            is_in[next] = False
            
N, M = map(int, stdin.readline().split())
node = [[0 for _ in range(N + 1)] for i in range(N + 1)]
can_go = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b , cost= map(int, stdin.readline().split())
    node[a][b] = cost
    node[b][a] = cost
    can_go[a].append(b)
    can_go[b].append(a)

for _ in range(M):
    a, b = map(int, stdin.readline().split())

    is_in = [False for _ in range(N + 1)]
    is_in[a] = True
    dfs(a, b, 0)
    