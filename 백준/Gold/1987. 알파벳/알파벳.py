from sys import stdin

def dfs(x, y):
    global cnt
    global ans

    if  cnt > ans:
        ans = cnt

    for nx, ny in [ (x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]:
        if nx >= 0 and ny >= 0 and nx < c and ny < r:
            if not used[ord(board[ny][nx]) - 65]:
                used[ord(board[ny][nx]) - 65] = True
                cnt += 1
                dfs(nx, ny)
                cnt -= 1
                used[ord(board[ny][nx]) - 65] = False

r, c = map(int, stdin.readline().split())
board = [[] for i in range(r)]
used = [False for i in range(26)]

global cnt
global ans

cnt = 1
ans = 1

for i in range(r):
    s = stdin.readline()
    board[i] = list(s)

used[ord(board[0][0]) - 65] = True
dfs(0,0)

print(ans)