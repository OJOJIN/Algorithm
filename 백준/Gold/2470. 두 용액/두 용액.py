from sys import stdin

N = int(stdin.readline())
waters = list(map(int, stdin.readline().split()))
waters.sort()

front = 0
back = N - 1

min = 2000000001
ans=[0,0]

while front < back:
    if min > abs(waters[front] + waters[back]):
        min = abs(waters[front] + waters[back])
        ans[0] = waters[front] 
        ans[1] = waters[back]

    if waters[front] + waters[back] < 0:
        front +=1
    else:
        back -= 1

print(ans[0], ans[1])