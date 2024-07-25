from sys import stdin
from math import sqrt

input = stdin.readline

MAX_NUM = 123456 * 2

def calc_sosu():
    for i in range(2, int(sqrt(MAX_NUM))+1):
        num = 2 * i
        while num <= MAX_NUM:
            is_sosu[num] = False
            num += i

is_sosu = [True] * (MAX_NUM+1)
is_sosu[1] = False
input_num = []
ans = []

calc_sosu()

while True:
    n = int(input())

    if n == 0:
        break

    input_num.append(n)


for num in input_num:
    cnt = 0
    for j in range(num+1, (2*num)+1):
        if is_sosu[j]:
            cnt += 1
    ans.append(cnt)

for a in ans:
    print(a)
    