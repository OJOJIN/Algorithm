from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())

line = deque(list(map(int, stdin.readline().split())))
robot = deque([False] * (2 * N + 1))

zero_cnt = 0
cnt = 0

while zero_cnt < K:

    cnt +=1
    zero_cnt = 0

    line.rotate(1)
    robot.rotate(1)

    if robot[N - 1] == True:
        robot[N - 1] = False

    for i in range(N - 2, -1, -1):
        if robot[i] and line[i + 1] > 0 and not robot[i + 1]:
            robot[i] = False
            robot[i + 1] = True
            line[i + 1] -= 1
    
    if robot[N - 1] == True:
        robot[N - 1] = False

    if line[0] > 0:
        line[0] -= 1
        robot[0] = True

    for i in line:
        if i == 0:
            zero_cnt += 1

print(cnt)  
