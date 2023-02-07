from sys import stdin

n = int(stdin.readline())

waters = list(map(int, stdin.readline().split()))

min = 2000000001
ans = [0, 0]

front = 0
last = n - 1

while front != last:
    dif = waters[front] + waters[last]
    if abs(dif - 0) < min:
        min = abs(dif - 0)
        ans[0] = front
        ans[1] = last
    
    if min == 0:
        break
    elif dif > 0:
        last -= 1
    else:
        front += 1

print(waters[ans[0]], waters[ans[1]])
