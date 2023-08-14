from sys import stdin

s = set()

N = int(stdin.readline())
list_num = list(map(int, stdin.readline().split()))
for i in list_num:
    s.add(i)
    
M = int(stdin.readline())
search_nums = list(map(int, stdin.readline().split()))

for num in search_nums:
    if num in s:
        print(1)
    else:
        print(0)
    