from collections import deque

visited = [False] * 100001
count = [0] * 100001
cnt = 0
min = 100000

n, k = map(int, input().split())


visited[n] = True
queue = deque()
queue.append([n, 0])

while queue:
    current = queue.popleft()
    if min < current[1]:
        break

    if current[0] == k:
        if min == 100000:
            min = current[1]
            cnt += 1
        elif min == current[1]:
            cnt += 1

    if current[0] * 2 <= 100000:
        if not visited[current[0] * 2] or count[current[0] * 2] == current[1] + 1:
            visited[current[0] * 2] = True
            queue.append([current[0] * 2, current[1] + 1])
            count[current[0] * 2] = current[1] + 1

    if current[0] + 1 <= 100000:
        if not visited[current[0] + 1] or count[current[0] + 1] == current[1] + 1:
            visited[current[0] + 1] = True
            queue.append([current[0] + 1, current[1] + 1])
            count[current[0] + 1] = current[1] + 1

    if current[0] - 1 >= 0:
        if not visited[current[0] - 1] or count[current[0] - 1] == current[1] + 1:
            visited[current[0] - 1] = True
            queue.append([current[0] - 1, current[1] + 1])
            count[current[0] - 1] = current[1] + 1

print(min)
print(cnt)
