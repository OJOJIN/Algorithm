from sys import stdin

input = stdin.readline

def find_head():
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                return (i,j)


def calc_waist_length(head_position):
    waist_length = 0
    for i in range(head_position[0] + 2, N):
        if board[i][head_position[1]] == '*':
            waist_length += 1
        else:
            break
    return waist_length

def calc_arms_length(head_position):
    left_arm_length = 0
    right_arm_length = 0
    for i in range(N):
        if board[head_position[0]+1][i] == '*' and i < head_position[1]:
            left_arm_length += 1
        elif board[head_position[0]+1][i] == '*' and i > head_position[1]:
            right_arm_length += 1
    return (left_arm_length, right_arm_length)

def calc_legs_length(head_position):
    left_leg_length = 0
    right_leg_length = 0
    for i in range(N):
        if N - i - 1 == head_position[0] + 1:
            break
        if board[N-i-1][head_position[1]-1] == '*':
            left_leg_length += 1
        if board[N-i-1][head_position[1]+1] == '*':
            right_leg_length += 1
    return (left_leg_length, right_leg_length)

N = int(input())

board = [list(input()) for _ in range(N)]

head_position = find_head()
waist_length = calc_waist_length(head_position)
left_arm_length, right_arm_length = calc_arms_length(head_position)
left_leg_legth, right_leg_length = calc_legs_length(head_position)
print(head_position[0] + 2, head_position[1] + 1)
print(left_arm_length, right_arm_length, waist_length, left_leg_legth, right_leg_length)
