

board = [[None] * 3 for _ in range(3)]

print board
while True:
    spot = [int(x) for x in raw_input().split()]
    board[spot[1]][spot[0]] = 'x'
    print board
