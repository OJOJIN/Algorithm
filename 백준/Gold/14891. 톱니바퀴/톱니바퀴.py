from sys import stdin
from collections import deque

def rotate_circle(original_num, num, direction):
    if num + 1 < 4 and num + 1 != original_num:
        if circle[num][2] != circle[num + 1][6]:
            rotate_circle(num, num+1, direction * -1)
    if num - 1 >= 0 and num - 1 != original_num:
        if circle[num][6] != circle[num - 1][2]:
            rotate_circle(num, num-1, direction * -1)
    
    circle[num].rotate(direction)

circle = []
ans = 0

for _ in range(4):
    s = stdin.readline().rstrip()
    circle.append(deque([int(x) for x in list(s)]))

K = int(stdin.readline())

for i in range(K):
    a, b = map(int, stdin.readline().split())
    rotate_circle(-1, a - 1, b)

for i in range(4):
    ans += circle[i][0] * pow(2, i)

print(ans)
