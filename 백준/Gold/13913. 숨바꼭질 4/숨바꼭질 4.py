from collections import deque

n, m = map(int, input().split())

visited = [-1] * 100001
before = [0] * 100001

que = deque()

que.append(n)
visited[n] = 0
while que:
    a = que.popleft()
    
    if(a == m):
        break
    
    for nx in [a + 1, a - 1, a * 2]:
        if 0 <= nx <= 100000 and visited[nx] < 0:
            visited[nx] = visited[a] + 1
            before[nx] = a
            que.append(nx)

ans = deque()

while m != n:
    ans.appendleft(m)
    m = before[m]

ans.appendleft(n)

print(len(ans) - 1)
for i in ans:
    print(i, end = " ")