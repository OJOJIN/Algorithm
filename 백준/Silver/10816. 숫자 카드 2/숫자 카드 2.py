from sys import stdin
from collections import Counter

N = int(stdin.readline())
have_card = map(int, stdin.readline().split())
M = int(stdin.readline())
check_card = map(int, stdin.readline().split())

counter = Counter(have_card)

for num in check_card:
    print(counter[num], end=" ")