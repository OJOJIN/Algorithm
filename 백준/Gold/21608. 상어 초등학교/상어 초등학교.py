from sys import stdin

def calculate_score(y, x, child):
    like_person = 0
    like_empty = 0
    for nx, ny in [(x + 1 , y), (x - 1 , y), (x , y - 1), (x, y + 1)]:
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if board[ny][nx] == 0:
                like_empty += 1
            elif board[ny][nx] in child:
                like_person += 1
    return (like_person, like_empty)

def calculate_like_score(y, x, child):
    like_person = 0
    for nx, ny in [(x + 1 , y), (x - 1 , y), (x , y - 1), (x, y + 1)]:
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if board[ny][nx] in child:
                like_person += 1
    if like_person == 0:
        return 0
    if like_person == 1:
        return 1
    if like_person == 2:
        return 10
    if like_person == 3:
        return 100
    if like_person == 4:
        return 1000
    
N = int(stdin.readline())
board = [[0 for i in range(N)] for _ in range(N)]
childs = []
child_like = [[] for _ in range(N*N + 1)]

for i in range(N * N):
    child = list(map(int, stdin.readline().split()))
    childs.append(child)
    child_like[child[0]] = child

for child in childs:
    high_score = [-1, -1, 0, 0]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                score = calculate_score(i, j, child)
                if score[0] > high_score[0]:
                    high_score[0] = score[0]
                    high_score[1] = score[1]
                    high_score[2] = i
                    high_score[3] = j
                elif score[0] == high_score[0] and score[1] > high_score[1]:
                    high_score[0] = score[0]
                    high_score[1] = score[1]
                    high_score[2] = i
                    high_score[3] = j
    board[high_score[2]][high_score[3]] = child[0]

ans = 0

for i in range(N):
    for j in range(N):
        ans += calculate_like_score(i, j, child_like[board[i][j]])
    
print(ans)
