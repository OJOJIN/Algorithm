import sys

S = input()
T = input()

while(len(T) >= len(S)):
    if S == T:
        print(1)
        exit(0)

    t = T.strip()[-1]
    T= T[:-1]
    if t == 'B':
        T = T[::-1]

print(0)
