N, M = map(int, input().split())
n = 0
i = 0

if M == 1:
    print("YES")
    exit(0)


while True:
    if M <= N and N <= M + i:
        print("YES")
        exit(0)
    if M > N:
        break
    M = M * 2 - 1
    n += 1
    i += pow(2, n)
    
print("NO")
