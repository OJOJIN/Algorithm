from sys import stdin
from copy import deepcopy

input = stdin.readline

def check_board_color(y, x, d):
    dy, dx = move_d[d]
    y = y + dy
    x = x + dx
    if 0 <= y < N and 0 <= x < N:
        return board[y][x]
    else:
        return 2
    
def is_stack(horse_num):
    for i in range(K):
        if not i in horse_stack[horse_num]:
            if horse[horse_num][0] == horse[i][0] and horse[horse_num][1] == horse[i][1]:
                return True
    return False

def stacking(horse_num):
    for i in range(K):
        if not i in horse_stack[horse_num]:
            if horse[horse_num][0] == horse[i][0] and horse[horse_num][1] == horse[i][1]:
                new_stack = []
                for j in horse_stack[i]:
                    new_stack.append(j)
                for j in horse_stack[horse_num]:
                    new_stack.append(j)
                for j in new_stack:
                    is_horse_bot[j] = False
                for k in new_stack:
                    horse_stack[k] = deepcopy(new_stack)
                is_horse_bot[horse_stack[horse_num][0]] = True

def move(horse_num):
    horse_unit = horse[horse_num]
    next_board_color = check_board_color(horse_unit[0], horse_unit[1], horse_unit[2])
    if next_board_color == 0:
        dy, dx = move_d[horse_unit[2]]
        for h_num in horse_stack[horse_num]:
            horse[h_num][0] += dy
            horse[h_num][1] += dx
        if is_stack(horse_num):
            stacking(horse_num)
            
    elif next_board_color == 1:
        dy, dx = move_d[horse_unit[2]]
        for h_num in horse_stack[horse_num]:
            horse[h_num][0] += dy
            horse[h_num][1] += dx
        reverse_list = []
        for h_num in horse_stack[horse_num]:
            is_horse_bot[h_num] = False
            reverse_list.append(h_num)
        for h_num in reverse_list:
            horse_stack[h_num].reverse()

        is_horse_bot[horse_stack[horse_num][0]] = True
        if is_stack(horse_num):
            stacking(horse_num)
    else:
        horse[horse_num][2] = oposite_d[horse[horse_num][2]]
        if check_board_color(horse[horse_num][0], horse[horse_num][1], horse[horse_num][2]) < 2:
            move(horse_num)

def solve():
    T = 0
    while T <= 1000:
        T += 1
        for i in range(K):
            if is_horse_bot[i]:
                move(i)
        for i in range(K):
            if len(horse_stack[i]) >= 4:
                print(T)
                exit(0)
    print(-1)

N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
horse = [list(map(int, input().split())) for _ in range(K)]

for i in range(K):
    horse[i][0] -= 1
    horse[i][1] -= 1

horse_stack = [[i] for i in range(K)]
is_horse_bot = [True for _ in range(K)]


move_d = {1:(0, 1), 2:(0, -1), 3:(-1, 0), 4:(1, 0)}
oposite_d = {1:2, 2:1, 3:4, 4:3}

solve()
