import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

# loop until the user says 'done' or dies
while True:

    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

    command = input('what is your command? ')  # get the command from the user
    if command == 'done':
        break  # exit the game
    elif command in ['left','l','west','w']:
        player_j -= 1  # move left
        if player_j not in range(len(board[0])):
            print("Can't go there!")
            player_j += 1
    elif command in ['right','r','east','e']:
        player_j += 1  # move right
        if player_j not in range(len(board[0])):
            print("Can't go there!")
            player_j -= 1
    elif command in ['up','u','north','n']:
        player_i -= 1  # move up
        if player_i not in range(len(board)):
            print("Can't go there!")
            player_i += 1
    elif command in ['down','d','south','s']:
        player_i += 1  # move down
        if player_i not in range(len(board)):
            print("Can't go there!")
            player_i -= 1

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break

            # print out the board
