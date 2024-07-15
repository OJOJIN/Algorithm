from sys import stdin

input = stdin.readline

T = int(input())

for t in range(1, T+1):
    line = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 21):
        for j in line[1:i+1]:
            if j > line[i]:
                cnt +=1 

    print(t, cnt)
