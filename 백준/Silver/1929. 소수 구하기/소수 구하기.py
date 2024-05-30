from sys import stdin

m, n = map(int, stdin.readline().split())

sosu = [True for _ in range(1000001)]
sosu[1] = False

for i in range(2, 1000001):
    if sosu[i]:
        for j in range(2,1000000):
            if i*j > 1000000:
                break
            sosu[i*j] = False

for i in range(m, n+1):
    if sosu[i]:
        print(i)