

board = [[None] * 3 for _ in range(3)]

print board
while True:
    x, y = [int(x) for x in raw_input().split()]
    board[y][x] = 'x'
    print board
