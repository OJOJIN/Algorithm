from sys import stdin
from copy import deepcopy

input = stdin.readline

def dfs(n, cur_sum, now_visited):
    global ans 
    if ans < cur_sum:
        return
    if len(now_visited) == N:
        ans = min(ans, cur_sum)
        return
    if now_visited in line_store[n]:
        if cur_sum < line_sum_store[n][line_store[n].index(now_visited)]:
            line_sum_store[n][line_store[n].index(now_visited)] = cur_sum
            for i in range(N):
                if i == n:
                    continue
                if i in now_visited:
                    dfs(i, cur_sum + line[n][i], deepcopy(now_visited))
                else:
                    now_visited.add(i)
                    dfs(i, cur_sum + line[n][i], deepcopy(now_visited))
                    now_visited.remove(i)
        else:
            return
    else:
        line_store[n].append(deepcopy(now_visited))
        line_sum_store[n].append(cur_sum)
        for i in range(N):
            if i == n:
                continue
            if i in now_visited:
                dfs(i, cur_sum + line[n][i], deepcopy(now_visited))
            else:
                now_visited.add(i)
                dfs(i, cur_sum + line[n][i], deepcopy(now_visited))
                now_visited.remove(i)

N, K = map(int, input().split())

line = [list(map(int, input().split())) for _ in range(N)]
line_store = [[] for _ in range(N)]
line_sum_store = [[] for _ in range(N)]

ans = 1000000000

dfs(K, 0, set([K]))

print(ans)
