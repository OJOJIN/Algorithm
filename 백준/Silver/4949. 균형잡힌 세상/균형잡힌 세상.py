from sys import stdin
from collections import deque

line = stdin.readline()

while line != ".":
    que = deque()
    if line[0] == ".":
        break

    ans = "yes"

    for i in line:
        if i == "(" or i == "[":
            que.append(i)
        if i == ")":
            if not que or que.pop() != "(":
                ans = "no"
        if i == "]":
            if not que or que.pop() != "[":
                ans = "no"
        if i == ".":
            if que:
                ans = "no"
            break
        
    print(ans)
    line = stdin.readline()       
    