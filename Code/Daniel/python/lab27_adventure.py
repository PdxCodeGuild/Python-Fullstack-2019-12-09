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
    enemy_i = random.randint(0, height - 1) # determin the X value of the enemies
    enemy_j = random.randint(0, width - 1) #determin the Y value of the enemies
    board[enemy_i][enemy_j] = '§' #represents the enemy

# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ').lower()  # get the command from the user

    if command in ['done' , 'quit' , 'end']:
        break  # exit the game
    elif command in ['left', 'west', 'w', 'l']:
        if player_j != 0:
            player_j -= 1  # move left
        elif player_j == 0:
            player_j += 9 # loop back to the right side of the map
    elif command in ['right', 'east', 'e', 'r']:
        if player_j != width-1:
            player_j += 1  # move right
        elif player_j == width-1:
            player_j -= 9 # loop back to the left
    elif command in ['north', 'n', 'up', 'u']:
        print(player_i)
        if player_i != 0:
            player_i -= 1  # move up
        elif player_i == 0:
            player_i += 9 # loop to the bottom
    elif command in ['south', 's', 'down', 'u']:
        print(player_i)
        if player_i != height-1:
            player_i += 1  # move down
        elif player_i == height-1:
            player_i -= 9 # loop to the top

        

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§': # if you're sitting on an enemy
        print('you\'ve encountered an enemy!') # telling the player they're sitting on an enemy
        action = input('what will you do? ') # ask them what they want to go
        if action == 'attack':
            print('you\'ve slain the enemy') # tell them they killed the enemy
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain') # tell them they suck and they died
            break

            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()