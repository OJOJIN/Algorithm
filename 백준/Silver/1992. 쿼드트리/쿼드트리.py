from sys import stdin

def check_quad(x, y, width):
    is_same = True

    for i in range(y, y + width):
        for j in range(x, x + width):
            if not board[y][x] == board[i][j]:
                is_same = False
            
    if is_same:
        print(board[y][x], end="")
        return
    else:
        print("(", end="")
        for nx, ny in (x, y), (x + int(width / 2), y), (x, y + int(width / 2)), (x + int(width / 2), y + int(width / 2)):
            check_quad(nx, ny, int(width / 2))

    print(")", end="")

N = int(stdin.readline())
board = []
for _ in range(N):
    board.append(stdin.readline())

check_quad(0, 0, N)