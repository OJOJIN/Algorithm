from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())

beforeStageSum = [0] * (n + 1)
afterStageNum = [[] for i in range(n + 1)]

for i in range(m):
    inputOrder = list(map(int, stdin.readline().split()))
    for j in range(1, len(inputOrder)):
        beforeStageSum[inputOrder[j]] += j - 1
        for k in range(j, len(inputOrder) - 1):
            afterStageNum[inputOrder[j]].append(inputOrder[k + 1])

stageOrder = deque()

for i in range(1, n + 1):
    if beforeStageSum[i] == 0:
        stageOrder.appendleft(i)

ansOrder = []
while stageOrder:
    stage = stageOrder.pop()
    ansOrder.append(stage)

    for i in afterStageNum[stage]:
        beforeStageSum[i] -= 1
        if beforeStageSum[i] == 0:
            stageOrder.appendleft(i)

if len(ansOrder) == n:
    for ans in ansOrder:
        print(ans)
else:
    print(0)
