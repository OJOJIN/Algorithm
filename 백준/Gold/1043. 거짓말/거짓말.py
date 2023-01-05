from sys import stdin

def dfs(num):
    for i in range(1, total_people + 1):
        if graph[num][i] and can_lie[i]:
            can_lie[i] = False
            dfs(i)

total_people, total_party = map(int, stdin.readline().split())
know_people_list = list(map(int, stdin.readline().split()))
graph = [[False for j in range(total_people + 1)]
         for i in range(total_people + 1)]
can_lie = [True] * (total_people + 1)
party_people_list = [[] for i in range(total_party)]

for i in know_people_list[1:]:
    can_lie[i] = False

lie_count = 0

for i in range(total_party):
    party_people_list[i] = list(map(int, stdin.readline().split()))
    for j in range(1, len(party_people_list[i]) - 1):
        for k in range(j + 1, len(party_people_list[i])):
            graph[party_people_list[i][j]][party_people_list[i][k]] = True
            graph[party_people_list[i][k]][party_people_list[i][j]] = True

for i in know_people_list[1:]:
    dfs(i)

for i in range(total_party):
    counting = True
    for j in party_people_list[i][1:]:
        if not can_lie[j]:
            counting = False
            break
    if counting:
        lie_count += 1

print(lie_count)