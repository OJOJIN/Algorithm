from sys import stdin

input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ans = 0

nums.sort()

for i in range(N):
    cur = nums[i]
    start = 0
    end = N - 1
    while start < end:
        if nums[start] + nums[end] == cur:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                ans += 1
                break
        elif nums[start] + nums[end] < cur:
            start += 1
        elif nums[start] + nums[end] > cur:
            end -= 1
            
print(ans)
                