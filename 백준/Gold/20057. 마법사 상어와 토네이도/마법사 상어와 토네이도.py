def tornado():
    y = N // 2
    x = N // 2
    dist = 1
    d_index = 0
    move_cnt = 0

    while True:
        for i in range(dist):
            dy, dx = d[d_index]
            move_y = y + dy
            move_x = x + dx
            if move_y == 0 and move_x == -1:
                return
            move_sand(move_y, move_x, d_index)
            y = move_y
            x = move_x
        move_cnt += 1
        d_index = (d_index + 1) % 4
        if move_cnt >= 2:
            move_cnt = 0
            dist += 1


def move_sand(y, x, d_index):
    global ans
    locations = move_sand_location(y, x, d_index)
    total_move_amount = 0

    for nx, ny, percent in locations:
        sand = int(board[y][x] * percent)
        if sand > 0:
            total_move_amount += sand
            if 0 <= ny < N and 0 <= nx < N:
                board[ny][nx] += sand
            else:
                ans += sand
    dy, dx = d[d_index]
    Y = y + dy
    X = x + dx

    if 0 <= Y < N and 0 <= X < N:
        board[Y][X] += board[y][x] - total_move_amount
    else:
        ans += board[y][x] - total_move_amount


def move_sand_location(y, x, d_index):
    if d_index == 0:
        return [(x - 2, y, 0.05), (x - 1, y - 1, 0.1), (x - 1, y + 1, 0.1), (x, y - 1, 0.07), (x, y + 1, 0.07),
                (x, y - 2, 0.02), (x, y + 2, 0.02), (x + 1, y + 1, 0.01), (x + 1, y - 1, 0.01)]
    elif d_index == 1:
        return [(x, y + 2, 0.05), (x + 1, y + 1, 0.1), (x - 1, y + 1, 0.1), (x - 1, y, 0.07), (x + 1, y, 0.07),
                (x - 2, y, 0.02), (x + 2, y, 0.02), (x + 1, y - 1, 0.01), (x - 1, y - 1, 0.01)]
    elif d_index == 2:
        return [(x + 2, y, 0.05), (x + 1, y - 1, 0.1), (x + 1, y + 1, 0.1), (x, y - 1, 0.07), (x, y + 1, 0.07),
                (x, y - 2, 0.02), (x, y + 2, 0.02), (x - 1, y + 1, 0.01), (x - 1, y - 1, 0.01)]
    else:
        return [(x, y - 2, 0.05), (x + 1, y - 1, 0.1), (x - 1, y - 1, 0.1), (x - 1, y, 0.07), (x + 1, y, 0.07),
                (x - 2, y, 0.02), (x + 2, y, 0.02), (x + 1, y + 1, 0.01), (x - 1, y + 1, 0.01)]

ans = 0
N = int(input())

board = []
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for i in range(N):
    board.append(list(map(int, input().split())))

tornado()

print(ans)

