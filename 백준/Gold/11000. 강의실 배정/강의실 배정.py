from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline())
lectures = []
end_times = []
ans = 0

for _ in range(N):
    lectures.append(list(map(int, stdin.readline().split())))

lectures.sort(key=lambda x:x[0])

for i in range(N):
    if end_times:
        first_end = heappop(end_times)
        if first_end > lectures[i][0]:
            heappush(end_times, lectures[i][1])
            heappush(end_times, first_end)
            ans+=1
        else:
            heappush(end_times, lectures[i][1])   
    else:
        ans+=1
        heappush(end_times, lectures[i][1])

print(ans)
