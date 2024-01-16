from sys import stdin

def move_ball(x, y, s, d):
    if d == 0:
        return (x, (y - s + N) % N)
    if d == 1:
        return ((x + s) % N, (y - s + N) % N)
    if d == 2:
        return ((x + s) % N, y)
    if d == 3:
        return ((x + s) % N, (y + s) % N)
    if d == 4:
        return (x, (y + s) % N)
    if d == 5:
        return ((x - s + N) % N, (y + s) % N)
    if d == 6:
        return ((x - s + N) % N, y)
    if d == 7:
        return ((x - s + N) % N, (y - s + N) % N)

def ball_composition(c_balls):
    total_weight = 0
    total_speed = 0

    for ball in c_balls:
        total_weight += ball[2]
        total_speed += ball[3]

    new_weight = int(total_weight / 5)

    if new_weight == 0:
        return []

    new_speed = int(total_speed / len(c_balls))

    first_direction = c_balls[0][4] % 2
    direction = True

    for ball in c_balls:
        if ball[4] % 2 != first_direction:
            direction = False
            break

    if direction:
        return [[c_balls[0][0], c_balls[0][1], new_weight, new_speed, 0],
                [c_balls[0][0], c_balls[0][1], new_weight, new_speed, 2],
                [c_balls[0][0], c_balls[0][1], new_weight, new_speed, 4],
                [c_balls[0][0], c_balls[0][1], new_weight, new_speed, 6]]
    else:
        return [[c_balls[0][0], c_balls[0][1], new_weight, new_speed, 1],
                [c_balls[0][0], c_balls[0][1], new_weight, new_speed, 3],
                [c_balls[0][0], c_balls[0][1], new_weight, new_speed, 5],
                [c_balls[0][0], c_balls[0][1], new_weight, new_speed, 7]]
    

N, M, K = map(int, stdin.readline().split())

balls = []


for i in range(M):
    ball = list(map(int, stdin.readline().split()))
    ball[0] -= 1
    ball[1] -= 1
    balls.append(ball)


while K > 0:
    K -= 1
    board = [[[] for i in range(N + 1)] for _ in range(N + 1)]
    for ball in balls:
        position = move_ball(ball[1], ball[0], ball[3], ball[4])
        ball[0] = position[1]
        ball[1] = position[0]
        board[position[0]][position[1]].append(ball)
    
    balls = []

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) == 1:
                balls.append(board[i][j][0])
            elif len(board[i][j]) > 1:
                new_balls = ball_composition(board[i][j])
                for new_ball in new_balls:
                    balls.append(new_ball)

ans = 0

for ball in balls:
    ans += ball[2]
    
print(ans)
