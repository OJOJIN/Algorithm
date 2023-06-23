from sys import stdin

N, Q = map(int, stdin.readline().split())
wood = list()
p = [i for i in range(N)]

for i in range(N):
    arr = list(map(int, stdin.readline().split()))
    wood.append([arr[0], arr[1], i])

wood.sort(key=lambda x: x[0])

idx = wood[0][2]
end = wood[0][1]
for i in range(1, N):
    if end >= wood[i][0]:
        p[wood[i][2]] = idx
        end = max(end, wood[i][1])
    else:
        idx = wood[i][2]
        end = wood[i][1]

for i in range(Q):
    a, b = map(int, stdin.readline().split())
    if p[a - 1] == p[b - 1]:
        print(1)
    else:
        print(0)
