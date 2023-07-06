from sys import stdin
        

n, s = map(int, stdin.readline().split())
line = list(map(int, stdin.readline().split()))

ans = n + 1

left, right = 0, 0

sub_sum = line[0]

while True:
    if sub_sum >= s:
        ans = min(ans, right - left + 1)
        sub_sum -= line[left]
        left += 1
    else:
        right += 1
        if right == n:
            break
        sub_sum += line[right]
    
    
if ans == n + 1:
    print(0)
else:
    print(ans)