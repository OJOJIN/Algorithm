from sys import stdin

input = stdin.readline

N = int(input())

building = list(map(int, input().split()))
razer_in = [0] * N

building_list = [(100000001, 0)]

for i in range(N):
    while building_list[-1][0] < building[i]:
        building_list.pop()
    razer_in[i] = building_list[-1][1]
    building_list.append((building[i], i+1))

print(*razer_in)
