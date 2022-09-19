from math import floor, ceil

#Recursive solver
def solve(board):

	#Current cell. initialize to (-1,-1)
	cell = (-1,-1)

	#Find nearest empty cell. empty cells contain 0.
	for i,row in enumerate(board):
		for j,col in enumerate(row):
			if col == 0:
				cell = (i,j)
				break
	
	#If board completely full, return it
	if cell == (-1,-1):
		return board


	#Next section is invalid numbers
	invalid = [] 
	
	#Handle numbers in the cell's row
	c_row = board[cell[0]]
	for c in c_row:
		invalid.append(c)


	#handle numbers in cell's column
	c_col = [row[cell[1]] for row in board]
	for c in c_col:
		invalid.append(c)


	#Handle numbers in cell's square

	#Get rows corresponding to cell's square
	c_sqr_rows = [row for i,row in enumerate(board) if floor(i/3) == floor(cell[0]/3)]

	#in those rows, get cols corresponding to cell's square
	c_sqr = [col for row in c_sqr_rows for j, col in  enumerate(row) if floor(j/3) == floor(cell[1]/3)]


	for c in c_sqr:
		invalid.append(c)

	#Construct valid list and handle exit condition
	valid = [i for i in range(1,10) if not i in invalid]

	if len(valid) == 0:
		return 

	#Recursive stage
	new_board = [[col for col in row] for row in board]	
	for v in valid:
		new_board[cell[0]][cell[1]] = v
		s = solve(new_board)
		if s:
			return s

if __name__ == "__main__":
	#Read board

	board = []
	with open('data.txt', 'r') as file:
		board = [[int(digit) for digit in row.split()] for row in file]


	#Solve and print
	sln = solve(board)
	
	for row in sln:
		print(' '.join([str(digit) for digit in row]))

				
