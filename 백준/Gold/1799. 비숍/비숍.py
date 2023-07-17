from sys import stdin
import time

global ans

def dfs(num, cnt, color):
    global ans
    if cnt > ans[color]:
        ans[color] = cnt
    if num >= n * n:
        return
    x = num % n
    y = int(num / n)
    
    if chess[y][x] == 1 and pruning(x,y):
        chess[y][x] = 2
        if n % 2 == 0: # 짝수n일 때 다음 줄 넘어가는거 처리
            if x == n - 1:
                dfs(num + 1, cnt + 1, color)
            elif x == n - 2:
                dfs(num + 3, cnt + 1, color)
            else:
                dfs(num + 2, cnt + 1, color)
        else:
            dfs(num + 2, cnt + 1, color)
        chess[y][x] = 1

    if n % 2 == 0: # 짝수n일 때 다음 줄 넘어가는거 처리
            if x == n - 1:
                dfs(num + 1, cnt, color)
            elif x == n - 2:
                dfs(num + 3, cnt, color)
            else:
                dfs(num + 2, cnt, color)
    else: 
        dfs(num + 2, cnt, color)

def pruning(x, y):
    for i in range(n):
        if y - i >= 0:
            ny = y - i  
            if x - i >= 0 and chess[ny][x - i] == 2:
                return False
            if x + i < n and chess[ny][x + i] == 2:
                return False
        else:
            break         
    return True

ans = [0, 0]
n = int(input())

chess = []

for _ in range(n):
    chess.append(list(map(int, stdin.readline().split())))

dfs(0, 0, 0)
dfs(1, 0, 1)

print(sum(ans))