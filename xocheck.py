board = [
		[1,2,1],
		[2,0,2],
		[1,0,0]
		]

def validate_board(board):
	len_validate = True
	cells_validate = True
	X_count = 0
	O_count = 0

	for row in board:
		if len(row)!= 3 or len(board)!=3:
			len_validate = False
		for cell in row:
			if cell==1:
				X_count+=1
			if cell==2:
				O_count+=1
			if not(0<=cell<=2):
				cells_validate = False

	XO_validate = (X_count==O_count) or (X_count-O_count==1)
	return len_validate and cells_validate and XO_validate

def game_finished(board):

	def check_free_cells():
		for row in board:
			for cell in row:
				if cell==0:
					return True
		return False
	
	def check_rows(player):
		for row in board:			
			if row[0]==row[1]==row[2]==player:
				return True
		return False

	def check_columns(player):
		for i in range(3):
			column = []		
			for j in range(3):
				column.append(board[j][i])
			if column[0]==column[1]==column[2]==player:
				return True
		return False

	def check_cross(player):
		if board[0][0]==board[1][1]==board[2][2]==player:
			return True
		if board[2][0]==board[1][1]==board[0][2]==player:
			return True
		return False

	def check_player_win(player):
		return check_rows(player) or check_columns(player) or check_cross(player)

	if check_player_win(1):
		return 1
	elif check_player_win(2):
		return 2
	elif check_free_cells():
		return 0
	else:
		return -1

def render_board(board):
	
	def tag(string, tag):
		return "<"+tag+">"+string+"</"+tag+">"
	def convert_cell(cell_value):
		if cell_value == 1:
			return "X"
		elif cell_value == 2:
			return "O"
		else:
			return "&nbsp"

	result_string = ""
	
	for row in board:
		current_row = ""
		for cell in row:
			current_row += tag(convert_cell(cell),"td")
		result_string += tag(current_row,"tr")

	return tag(result_string,"table")

def d(x):
	return print(x)



