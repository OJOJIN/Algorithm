from sys import stdin

input = stdin.readline

N, G = map(str, input().split())
game_num = {'Y':1, 'F':2, 'O':3}
players = set()

for i in range(int(N)):
    p = input().rstrip()
    players.add(p)

print(int(len(players)/game_num[G]))
