from sys import stdin
import math

t = int(stdin.readline())
while t > 0:
    ans = 0
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())

    r3 = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    if x1 == x2 and y1 == y2 and r1 == r2:
        ans = -1
    elif max(r1, r2) > r3:
        if r3 + min(r1, r2) > max(r1, r2):
            ans = 2
        elif r3 + min(r1, r2) == max(r1, r2):
            ans = 1
        else:
            ans = 0
    else:
        if r3 > r1 + r2:
            ans = 0
        elif r3 == r1 + r2:
            ans = 1
        else:
            ans = 2

    print(ans)

    t -= 1
