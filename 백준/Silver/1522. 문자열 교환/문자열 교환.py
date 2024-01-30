from sys import stdin

N = list(stdin.readline().rstrip())
cnt_a = 0
max_a = 0

for i in range(len(N)):
    if N[i] == 'a':
        cnt_a += 1

for i in range(len(N)):
    cur_cnt_a = 0
    for j in range(cnt_a):
        if N[(i + j) % len(N)] == 'a':
            cur_cnt_a += 1
    if cur_cnt_a > max_a:
        max_a = cur_cnt_a

print(cnt_a - max_a)