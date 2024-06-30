from sys import stdin

input = stdin.readline

move = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0), 
        'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}

king, stone, N = map(str, input().split())

king_position = [8 - int(king[1]), ord(king[0]) - 65]
stone_position = [8 - int(stone[1]), ord(stone[0]) - 65]

move_list = [input().rstrip() for i in range(int(N))]

for mv in move_list:
    dy, dx = move[mv]
    if 0 <= king_position[0] + dy < 8 and 0 <= king_position[1] + dx < 8:
        king_position[0] += dy
        king_position[1] += dx
        if king_position[0] == stone_position[0] and king_position[1] == stone_position[1]:
            if 0 <= stone_position[0] + dy < 8 and 0 <= stone_position[1] + dx < 8:
                stone_position[0] += dy
                stone_position[1] += dx
            else:
                king_position[0] -= dy
                king_position[1] -= dx
                
print(chr(65 + king_position[1]) + str(8 - king_position[0]))
print(chr(65 + stone_position[1]) + str(8 - stone_position[0]))
