import sys

input = sys.stdin.readline

N = list(map(int, input().split()))

s = 0
before_num = 0

for i in N:
    s += i

ans = []

while 1:
    hit = -1

    for i in range(9, -1, -1):
        if N[i] >= int(s/2) + 1 and before_num != i:
            ans.append(i)
            s -= 1
            N[i] -= 1
            before_num = i
            hit = 0
            break
    if hit == -1:
        for i in range(9, -1, -1):
            if N[i] > 0 and i != before_num:
                ans.append(i)
                s -= 1 
                N[i] -= 1
                before_num = i
                hit = 0
                break
    
    if hit == -1:
        break

if ans:
    print(*ans,sep="")
else:
    print(0)