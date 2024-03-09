from sys import stdin
from copy import deepcopy

def turn_switch(num):
    if num == N - 1:
        for n in (num-1), num:
            now_light[n] = (now_light[n] + 1) % 2
    elif num == 0:
        for n in num, num+1:
            now_light[n] = (now_light[n] + 1) % 2
    else:
        for n in (num-1), num, num+1:
            now_light[n] = (now_light[n] + 1) % 2

N = int(stdin.readline())
init_light = list(map(int, list(stdin.readline().rstrip())))
goal_light = list(map(int, list(stdin.readline().rstrip())))

now_light = deepcopy(init_light)
ans = -1
cnt_1 = 0
cnt_2 = 1

for i in range(1, N):
    if now_light[i - 1] == goal_light[i - 1]:
        continue
    turn_switch(i)
    cnt_1 += 1
if goal_light == now_light:
        if ans == -1:
            ans = cnt_1

now_light = deepcopy(init_light)
turn_switch(0)
for i in range(1, N):
    if now_light[i - 1] == goal_light[i - 1]:
        continue
    turn_switch(i)
    cnt_2 += 1
if goal_light == now_light:
        if ans > cnt_2 or ans == -1:
            ans = cnt_2
print(ans)