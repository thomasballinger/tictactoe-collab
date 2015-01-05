print 'best game ever'
def display(board):
	for i in range(0,3):
		line = ''
		for j in range(0,3):
			if(board[i][j] != None):
				line += board[i][j] + ' '
			else:
				line += ' | '
		print line
board = [[None] * 3 for _ in range(3)]
display(board)
while True:
    x, y = [int(x) for x in raw_input().split()]
    if 0 <= x <= 2 and 0 <= y <= 2:
        board[y][x] = 'x'
        display (board)

