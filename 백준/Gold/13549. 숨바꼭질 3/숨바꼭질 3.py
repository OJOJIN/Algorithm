from collections import deque

n, m = map(int, input().split())

visited = [9999999] * 2000002

que = deque()

que.append(n)
visited[n] = 0
while que:
    a = que.popleft()
    
    for nx in [a + 1, a - 1, a * 2]:
        if 0 <= nx <= 100000 and visited[nx] > visited[a]:
            if nx == a * 2:
                visited[nx] = visited[a]
            else:
                visited[nx] = visited[a] + 1
            que.append(nx)
        
print(visited[m])