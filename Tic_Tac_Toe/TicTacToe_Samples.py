import itertools

#method 1 for obtaining 2 numbers alternatively cyclic
players = [1, 0]

choice = 1

for i in range(10):
	current_player = choice 
	print(current_player)
	choice = players[choice]

#method 2 for obtaining 2 numbers alternatively cyclic
player_choice = itertools.cycle([1, 2])
print("\n")
for i in range(10):
	print(next(player_choice))

print("\n")

#method 1 for a string from an array
game_size = 3
s = "   "

for i in range(game_size):
	s += "  " + str(i) 

print(s)

#method 2 for a string from an array
s = "     " + "  ".join([str(i) for i in range(game_size)])
print(s)
print("\n")

#method 1 for creating 3x3 array
game = [[0 for i in range(game_size)] for i in range(game_size)]
print(game)

#method 2 for creating 3x3 array
new_game = []
for i in range(game_size):
	row = []
	for i in range(game_size):
		row.append(0)
	new_game.append(row)

print(new_game)
