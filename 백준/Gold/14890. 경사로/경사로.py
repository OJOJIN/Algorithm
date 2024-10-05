from sys import stdin

input = stdin.readline

def check_horizon_road(n):
    prev_h = board[n][0]
    cur_h = 0
    flat_cnt = 0
    i = 0
    while i < N:
        cur_h = board[n][i]
        if cur_h == prev_h:
            flat_cnt += 1
        elif cur_h == (prev_h + 1):
            if flat_cnt < L:
                return False
            flat_cnt = 1
            prev_h = cur_h
        elif cur_h == (prev_h - 1):
            for j in range(L):
                if N <= i + j:
                    return False
                if board[n][i+j] != cur_h:
                    return False
            i += (L - 1)
            flat_cnt = 0
            prev_h = cur_h
        else:
            return False
        
        i += 1

    return True

def check_vertical_road(n):
    prev_h = board[0][n]
    cur_h = 0
    flat_cnt = 0
    i = 0
    while i < N:
        cur_h = board[i][n]
        if cur_h == prev_h:
            flat_cnt += 1
        elif cur_h == (prev_h + 1):
            if flat_cnt < L:
                return False
            flat_cnt = 1
            prev_h = cur_h
        elif cur_h == (prev_h - 1):
            for j in range(L):
                if N <= i + j:
                    return False
                if board[i+j][n] != cur_h:
                    return False
            i += (L-1)
            flat_cnt = 0
            prev_h = cur_h
        else:
            return False
        
        i += 1

    return True

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    if check_horizon_road(i):
        ans += 1
    if check_vertical_road(i):
        ans += 1

print(ans)
