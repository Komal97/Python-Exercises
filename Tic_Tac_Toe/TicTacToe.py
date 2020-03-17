import itertools
from coloroma import init

init()

# count = 0 
# for row in game:
# 	print(count, row)
# 	count+=1

def win(game):

	def all_same(l):
		if(l.count(l[0])==len(l) and l[0]!=0):
			return True
		else:
			return False

	#Horizontal

	'''
	for row in game:
		print(row)
		all_match = True
		for item in row:
			if(item!=row[0] or row[0]==0):
				all_match=False
		if all_match:
			print("winner horizontally")

		'''
	for row in game:
		print(row)
		if all_same(row):
			  print(f"Player {row[0]} is the winner horizontally!!")
			  return True

	#Diagonal
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally (\\)!")
		return True

	# for idx in rows:
	# 	print(idx, cols[idx])
	# for col, row in zip(list(reversed(range(len(game)))), range(len(game))):
	# 	print(col, row)
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally (/)!")
		return True

	#Vertical
	for col in range(len(game)):
		check = []

		for row in game:
			check.append(row[col])

		if all_same(check):
			print(f"Player {check[0]} is the winner vertically!")
			return True

	return False

def game_board(game_map, player=0, row=0, column=0):
	try:
		if (row>2 or column>2 or row<0 or column<0):
			print("Position not available, please choose row and column between 0 to 2")
			return game_map,False
		elif(game_map[row][column] != 0):
			print("This position is already occupied, please choose another")
			return game_map,False

		print("   " + "  ".join([str(i) for i in range(len(game_map))]))

		if player!=0 :
			game_map[row][column]=player
		for count, row in enumerate(game_map):
			#print(count, row)

			coloured_row = " "
			for item in row:
				if item == 0 :
					coloured_row += " "
				elif item == 1 :
					coloured_row += FORE.GREEN + " X " + Style.RESET_ALL
				elif item == 2 :
					coloured_row += FORE.MAGENTA + " O " + Style.RESET_ALL
			print(count, coloured_row)

		print("\n")
		return game_map,True
	except Exception as e:
		print("Error : ", e)
		return game_map,False


play = True
while play:
	game_size = int(input("What size game of tic tac toe? "))
	game = [[0 for i in range(game_size)] for i in range(game_size)]
	
	game_won = False
	game,_ = game_board(game)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current player: {current_player}")
		played = False

		while not played:
			column_choice = int(input("What column do you want to play? (0,1,2): "))
			row_choice = int(input("What row do you want to play? (0,1,2): "))
			game, played = game_board(game, current_player, row_choice, column_choice)

		if win(game):
			game_won = True
			again = input("Do you want to play again? (y/n) ")
			if again.lower() == "y":
				print("restarting game...")
			elif again.lower() == "n":
				print("game over...")
				play = False
			else:
				print("Not a valid answer, game over...")
				play = False

			
