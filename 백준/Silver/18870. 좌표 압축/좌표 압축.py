from copy import deepcopy
N = int(input())
nums = list(map(int, input().split()))

original_nums = deepcopy(nums)

nums = list(set(nums))
nums.sort()
n = len(nums)

comp_nums = dict()


for i in range(n):
    comp_nums[nums[i]] = i

for i in range(N):
    print(comp_nums.get(original_nums[i]), end = " ")
