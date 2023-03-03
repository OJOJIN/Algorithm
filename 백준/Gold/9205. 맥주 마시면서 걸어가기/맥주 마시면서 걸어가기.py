from sys import stdin
from collections import deque

t = int(stdin.readline())

while t != 0:
    t -= 1
    n = int(stdin.readline())

    store = []
    que = deque()
    visited = [False] * n
    ans = "sad"

    que.append((map(int, stdin.readline().split())))
    
    for i in range(n):
        store.append(list(map(int, stdin.readline().split())))

    dep = list(map(int, stdin.readline().split()))

    while que:
        x, y = que.popleft()
        if abs(x - dep[0]) + abs(y - dep[1]) <= 1000:
            ans = "happy"
            break
        for i in range(n):
            if not visited[i] and abs(x - store[i][0]) + abs(y - store[i][1]) <= 1000:
                    que.append((store[i][0], store[i][1]))
                    visited[i] = True
    print(ans)
                