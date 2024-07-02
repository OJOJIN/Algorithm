from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

tree_list = list(map(int, input().split()))

start = 0

end = max(tree_list)

while start <= end:
    now_len = 0
    mid = (start + end) // 2
    for tree in tree_list:
        if (tree - mid) > 0:
            now_len += (tree - mid)

    if now_len >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(start-1)
