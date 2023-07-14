from sys import stdin

def union(a, b):
    a = find(a) 
    b = find(b)
    if a > b:
        parent[a] = b
    else :
        parent[b] = a

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def dfs(position, before):
    x = position % M
    y = int(position / M)
    
    if is_in[position]:
        is_in[position] = False
        union(position, before)
        dfs(next_position(x,y), parent[position])
    else:
        union(position, before)
    
def next_position(x, y):
    position = y*M + x
    if board[y][x]=='D':
        position += M
    elif board[y][x]=='U':
        position -= M
    elif board[y][x]=='R':
        position += 1
    elif board[y][x]=='L':
        position -= 1
    return position

board = []

N, M = map(int, stdin.readline().split())
parent = [i for i in range(N*M)]
group = set()
is_in = [True for _ in range(N*M)]

for _ in range(N):
    board.append(list(stdin.readline().rstrip()))

for position in range(N*M):
    if is_in[position]:
        dfs(position, position)

for i in range(N*M):
    group.add(find(i))

print(len(group))