import sys

def play_game():
    score = 0
    innings = 0
    n = 0
    while innings < N:
        out_count = 0
        base = []

        while out_count < 3:
            bat = player[n]
            if innings_result[innings][bat] == 0:
                out_count += 1
            else:
                base.append(innings_result[innings][bat])
            n = (n + 1) % 9
        base.reverse()
        remain = 3
        cnt = 0
        for hit in base:
            remain -= hit
            if remain < 0:
                break
            else:
                cnt += 1

        score += len(base) - cnt

        innings += 1
    return score

def select_proceduer(number):
    global ans
    if number > 8:
        for i in range(1,10):
            player[i - 1] = procedure.index(i)
        score = play_game()
        ans = max(ans, score)
        return
    else:
        for i in procedure_num:
            if not i in procedure:
                procedure[number] = i
                select_proceduer(number + 1)
                procedure[number] = 0

input = sys.stdin.readline

N = int(input())

ans = 0
player = [0,0,0,0,0,0,0,0,0]
innings_result = []
base = [False, False, False]
procedure = [4,0,0,0,0,0,0,0,0]
procedure_num = [1,2,3,5,6,7,8,9]

for i in range(N):
    result = list(map(int, input().split()))
    innings_result.append(result)

select_proceduer(1)
print(ans)