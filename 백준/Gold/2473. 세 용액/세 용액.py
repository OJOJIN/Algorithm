from sys import stdin

n = int(stdin.readline())

water = list(map(int, stdin.readline().split()))
water.sort()
min = 3000000000
ans = []
0
for i in range(n):
    l = 0
    r = n - 1
    while not l == r and not r == i and not l == i:
        if abs(water[i] + water[l] + water[r]) < min:
            min = abs(water[i] + water[l] + water[r])
            ans = list([water[i], water[l], water[r]])
            
        if water[i] + water[l] + water[r] > 0: 
            r -= 1

        elif water[i] + water[l] + water[r] < 0:
            l += 1

        else: break

    if min == 0:
        break

ans.sort()

for a in ans:
    print(a, end = " ")