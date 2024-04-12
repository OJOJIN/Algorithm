def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result

def calculate_score_diff(arr):
    score_1 = 0
    score_2 = 0
    opposit_arr = []
    for i in range(N):
        if not i in arr:
            opposit_arr.append(i)

    for i in range(N//2):
        for j in range(i + 1, N//2):
            score_1 += board[arr[i]][arr[j]]
            score_1 += board[arr[j]][arr[i]]
            score_2 += board[opposit_arr[i]][opposit_arr[j]]
            score_2 += board[opposit_arr[j]][opposit_arr[i]]
    return abs(score_1 - score_2)

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
arr = [i for i in range(N)]
ans = -1

combination = comb(arr, N//2)

for c in combination:
    score_diff = calculate_score_diff(c)
    if ans < 0 :
        ans = score_diff
    else:
        ans = min(ans, score_diff)

print(ans)