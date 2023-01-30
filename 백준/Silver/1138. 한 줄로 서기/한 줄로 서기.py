from sys import stdin
from queue import PriorityQueue

N = int(stdin.readline())

left = [-1] + list(map(int, stdin.readline().split()))

que = PriorityQueue()

for i in range(0, N):
    for num in range(1, N + 1):
        if left[num] == 0:
            que.put(num)
            break

    a = que.get()
    
    print(a, end = " ")
    for j in range(1, a + 1):
        left[j] -= 1