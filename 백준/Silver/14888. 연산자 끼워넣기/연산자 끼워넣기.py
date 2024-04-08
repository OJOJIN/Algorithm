def dfs(n, num):
    global min_ans
    global max_ans

    if n == N:
        min_ans = min(num, min_ans)
        max_ans = max(num, max_ans)
        return
    for op in range(4):
        if operator[op] > 0:
            operator[op] -= 1
            dfs(n + 1, calculate(num, nums[n], op))
            operator[op] += 1

def calculate(n1, n2, op):
    if op == 0:
        return n1 + n2
    elif op == 1:
        return n1 - n2
    elif op == 2:
        return n1 * n2
    else:
        if n1 >= 0:
            return n1 // n2
        else:
            return -(abs(n1) // n2)


N = int(input())

nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

min_ans = 1000000001
max_ans = -1000000001

dfs(1, nums[0])

print(max_ans)
print(min_ans)