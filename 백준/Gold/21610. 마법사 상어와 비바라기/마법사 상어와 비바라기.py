def move(di, s):
    d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    dy, dx = d[di-1]
    dy *= s
    dx *= s
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                y = i + dy
                x = j + dx
                while x < 0:
                    x += N
                while y < 0:
                    y += N
                x %= N
                y %= N
                before_cloud[y][x] = True
                board[y][x] += 1

def init_cloud():
    for i in range(N):
        for j in range(N):
            cloud[i][j] = False

def init_before_cloud():
    for i in range(N):
        for j in range(N):
            before_cloud[i][j] = False

def copy_water_bug():
    for i in range(N):
        for j in range(N):
            if before_cloud[i][j]:
                for ny, nx in (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1):
                    if 0 <= nx < N and 0 <= ny < N and board[ny][nx] > 0:
                        board[i][j] += 1

def make_cloud():
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not before_cloud[i][j]:
                cloud[i][j] = True
                board[i][j] -= 2

ans = 0
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magic = [list(map(int, input().split())) for _ in range(M)]

before_cloud = [[False for i in range(N)] for j in range(N)]
cloud = [[False for i in range(N)] for j in range(N)]

cloud[N-1][0] = True
cloud[N-1][1] = True
cloud[N-2][0] = True
cloud[N-2][1] = True

for d, s in magic:
    move(d, s)
    init_cloud()
    copy_water_bug()
    make_cloud()
    init_before_cloud()

for i in range(N):
    for j in range(N):
        ans += board[i][j]

print(ans)
