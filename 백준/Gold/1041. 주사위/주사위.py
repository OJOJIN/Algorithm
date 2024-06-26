from sys import stdin

input = stdin.readline

N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))
    exit(0)

three = [[0, 1, 2], [0, 1, 3], [0, 2, 4], [0, 3, 4],
         [5, 1, 2], [5, 1, 3], [5, 2, 4], [5, 3, 4]]
not_two = [[0, 5], [1, 4], [2, 3],
           [5, 0], [4, 1], [3, 2]]

min_two = 2000001
min_three = 3000001

for i in range(6):
    for j in range(6):
        if not [i, j] in not_two and i != j:
            min_two = min(min_two, dice[i] + dice[j])

for t in three:
    min_three = min(min_three, dice[t[0]] + dice[t[1]] + dice[t[2]])

ans = (min_two * ((N - 1) * 4 + (N - 2) * 4)) + (min_three * 4) + (min(dice) * (((N-2)**2) * 5 + (N - 2) * 4))

print(ans)
