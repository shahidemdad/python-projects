# Project: Tic-Tac-Toe
# ****Plan:****
# board
# display board
# play game
# handle turn (who goes first)[valid input]
# check win
    #check row
    #check column
    #check diagonals
# check tie
# flip players

# game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#If the game is still going
game_running = True

#who is the winner
winner = None

#who's turn
current_player = "X"

# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print(board[6] + " | " + board[7] + " | " + board[8])

# play game
def play_game():

    #display initial board
    display_board()

    #while the game is keep running
    while game_running:

        # handle turn: take turns untill one of the players win
        handle_turn(current_player)
        
        #check if the game is over
        game_result()
            
        #othersie flip players
        flip_players()
        
    #print out results
    if winner == "X" or winner == "O":
        print (winner + " has won the game.")
    elif winner == None:
        print("The game has tied.")

# handle turn (who goes first)[valid input]
def handle_turn(player):
    print(player + "'s turn now.")
    position = input("Choose the box(1-9) you want to start with: ")
    
    limited_input = ["1","2","3","4","5","6","7","8","9"]
    valid = False
    while not valid:
        while position not in limited_input:
            position = input("Invalid input. Please try again: ")
        position =  int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can not go there!:) Try again. ")
    board[position] = player
    display_board()

#check if the game is over
def game_result():
    check_win()
    check_tie()

#check if there is any win
def check_win():
    #set up global variables
    global winner
    #check rows
    row_winner = check_row()
    #check column
    column_winner = check_column()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None  
    return

#check row
def check_row():
    # set up global variables
    global game_running
    #check each rows
    row_1 = board[0] == board[1] == board [2] != "-"
    row_2 = board[3] == board[4] == board [5] != "-"
    row_3 = board[6] == board[7] == board [8] != "-"
    #if there is a match, means there is a win
    if row_1 or row_2 or row_3:
        game_running = False
    #who won X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

#check column
def check_column():
    # set up global variables
    global game_running
    #check each rows
    column_1 = board[0] == board[3] == board [6] != "-"
    column_2 = board[1] == board[4] == board [7] != "-"
    column_3 = board[2] == board[5] == board [8] != "-"
    #if there is a match, means there is a win
    if column_1 or column_2 or column_3:
        game_running = False
    #who won X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

#check diagonals
def check_diagonals():
    # set up global variables
    global game_running
    #check upleft to bottomright
    diagonal_1 = board[0] == board[4] == board [8] != "-"
    #check bottomleft to upright
    diagonal_2 = board[6] == board[4] == board [2] != "-"
    #if there is a match, means there is a win
    if diagonal_1 or diagonal_2:
        game_running = False
    #who won X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

#check if there is a tie
def check_tie():
    global game_running
    if "-" not in board:
        game_running = False
    return

# who is turn is to decide
def flip_players():
    #global variable set up
    global current_player

    #if the current player get to "X", then change to "O" for next player
    if current_player == "X":
        current_player = "O"
    #if the current player get to "O", then change to "X" for next player
    elif current_player == "O":
        current_player = "X"
    return

#final step to play the game
play_game()