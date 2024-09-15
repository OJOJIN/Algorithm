from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(num, w):
    max = 0
    check[num] = True

    for node, weight in tree[num].items():
        if not check[node]:
            max = dfs(node, weight)
            if max > max_child[num]:
                max_length[num] = max_child[num] + max
                max_child[num] = max
            elif max + max_child[num] > max_length[num]:
                max_length[num] = max + max_child[num]

    return w + max_child[num]


v = int(stdin.readline())

tree = [dict() for i in range(v + 1)]
max_child = [0] * (v + 1)
max_length = [0] * (v + 1)
check = [False] * (v + 1)
ans = 0

for i in range(1, v + 1):
    input_list = list(map(int, stdin.readline().split()))
    for j in range(1, len(input_list) - 1, 2):
        tree[input_list[0]][input_list[j]] = input_list[j + 1]

dfs(1, 0)

for i in range(1, v + 1):
    if max_length[i] > ans:
        ans = max_length[i]

print(ans)
