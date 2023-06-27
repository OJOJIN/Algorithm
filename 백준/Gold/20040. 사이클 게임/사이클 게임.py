from sys import stdin

n, m = map(int, stdin.readline().split())

p = [i for i in range(n)]


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


a_list = []
b_list = []

ans = 0

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    a_list.append(a)
    b_list.append(b)

for i in range(m):
    if find(a_list[i]) == find(b_list[i]):
        ans = i + 1
        break
    else:
        union(a_list[i], b_list[i])

print(ans)
