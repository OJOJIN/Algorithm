from sys import stdin
from collections import deque

T = int(stdin.readline())

while T > 0:
    forward = True
    T-=1

    s = stdin.readline().rstrip()
    N = int(stdin.readline())
    check_error = False

    command = stdin.readline().rstrip()
    if command == "[]":
        que = deque()
    else:
        que = deque(list(map(int,command[1:][0:-1].split(","))))
    
    for i in s:
        if i == "R":
            forward = not forward
        else:
            if que:
                if forward:
                    que.popleft()
                else:
                    que.pop()
            else:
                check_error = True

    if check_error:
        print("error")
    else:
        if que:
            ans = list(que)
            if not forward:
                ans.reverse()
            print("[",end="")
            for i in range(len(ans) - 1):
                print(str(ans[i])+",",end="")
            print(str(ans[-1])+"]")
        else:
            print("[]") 
    