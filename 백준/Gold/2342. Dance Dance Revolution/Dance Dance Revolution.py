from sys import stdin


def dp(num, sequence):
    save = [[0 for j in range(5)] for i in range(5)]
    count_save = [[-1 for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            if count[i][j] == sequence - 1 and (i != j or i == 0):
                if count_save[num][j] == sequence:
                    save[num][j] = min(save[num][j], ddr[i]
                                       [j] + weight(num, i))
                else:
                    save[num][j] = ddr[i][j] + weight(num, i)

                count_save[num][j] = sequence

                if count_save[i][num] == sequence:
                    save[i][num] = min(save[i][num], ddr[i]
                                       [j] + weight(num, j))
                else:
                    save[i][num] = ddr[i][j] + weight(num, j)

                count_save[i][num] = sequence

    for i in range(5):
        for j in range(5):
            if save[i][j] != 0:
                ddr[i][j] = save[i][j]
            if count_save[i][j] != -1:
                count[i][j] = sequence


def weight(current, before):
    if current == before:
        return 1
    if before == 0:
        return 2
    if abs(current - before) == 2:
        return 4
    return 3


count = [[-1 for j in range(5)] for i in range(5)]
ddr = [[999999 for j in range(5)] for i in range(5)]
ddr[0][0] = 0

seq = list(map(int, stdin.readline().split()))

ddr[seq[0]][0] = 2
ddr[0][seq[0]] = 2
count[seq[0]][0] = 0
count[0][seq[0]] = 0

for i in range(1, len(seq)):
    if seq[i] == 0:
        break
    dp(seq[i], i)

ans = 999999

for i in range(5):
    for j in range(5):
        if count[i][j] == len(seq) - 2:
            ans = min(ans, ddr[i][j])
if seq[0] == 0:
    ans = 0
print(ans)
