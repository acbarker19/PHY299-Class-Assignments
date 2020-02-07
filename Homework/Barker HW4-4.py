# HW 4-4
# Alec Barker

# a string containing instructions on how to play
instructions = """Tic Tac Toe
The grid will be split up in the following way:
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 | 9 |
    -------------
Enter the number that corresponds with the grid space that you wish to place your shape.
You may also type \"Quit\" at any point to end the game."""

# lists of each row
top = [" ", " ", " "]
middle = [" ", " ", " "]
bottom = [" ", " ", " "]

# list containing all rows
rows = [top, middle, bottom]

# keeps track if the game should end its loop
game_over = False

###############################################################################

def print_grid():
    """Prints the grid with the correct shape in the squares."""
    
    hor = "-------------"
    
    print("Current Grid:")
    for row in rows:
        print(hor)
        print("| {0} | {1} | {2} |".format(row[0], row[1], row[2]))
    print(hor)
    
def is_space_taken(num):
    """Checks if the space is already taken by another shape."""
    
    is_taken = False
    
    if num >= 1 and num <= 3:
        if top[num - 1] != " ":
            is_taken = True
    elif num >= 4 and num <= 6:
        if middle[num - 4] != " ":
            is_taken = True
    else:
        if bottom[num - 7] != " ":
            is_taken = True
    
    return is_taken

def set_space(num, shape):
    """Sets the player's shape in the specified grid space."""
    
    if num >= 1 and num <= 3:
        top[num - 1] = shape
    elif num >= 4 and num <= 6:
        middle[num - 4] = shape
    else:
        bottom[num - 7] = shape

def get_winner():
    """Checks for a winner or tie based on all winning patterns."""
    
    if(top[0] == top[1] and top[1] == top[2] and
       top[0] != " " and top[1] != " " and top[2] != " "):
        winner = top[0]
    elif(middle[0] == middle[1] and middle[1] == middle[2] and
         middle[0] != " " and middle[1] != " " and middle[2] != " "):
        winner = middle[0]
    elif(bottom[0] == bottom[1] and bottom[1] == bottom[2] and
         bottom[0] != " " and bottom[1] != " " and bottom[2] != " "):
        winner = bottom[0]
    elif(top[0] == middle[0] and middle[0] == bottom[0] and
         top[0] != " " and middle[0] != " " and bottom[0] != " "):
        winner = top[0]
    elif(top[1] == middle[1] and middle[1] == bottom[1] and
         top[1] != " " and middle[1] != " " and bottom[1] != " "):
        winner = top[1]
    elif(top[2] == middle[2] and middle[2] == bottom[2] and
         top[2] != " " and middle[2] != " " and bottom[2] != " "):
        winner = top[2]
    elif(top[0] == middle[1] and middle[1] == bottom[2] and
         top[0] != " " and middle[1] != " " and bottom[2] != " "):
        winner = top[0]
    elif(top[2] == middle[1] and middle[1] == bottom[0] and
         top[2] != " " and middle[1] != " " and bottom[0] != " "):
        winner = top[2]
    elif(top[0] != " " and top[1] != " " and top[2] != " " and
            middle[0] != " " and middle[1] != " " and middle[2] != " " and
            bottom[0] != " " and bottom[1] != " " and bottom[2] != " "):
        winner = "Tie"
    else:
        winner = "None"
    
    return winner

###############################################################################

# prints the instructions once for the player
print(instructions)

# creates a loop that continues until the game ends
while game_over == False:
    
    # creates a loop for player 1
    while True:
        # asks for input
        move = input("Player 1, please enter a grid number: ")
        
        # checks if the player wants to quit
        if move.lower() == "quit":
            game_over = True
            break
        
        # checks if the user input a valid digit
        elif move.isdigit() == False or int(move) < 1 or int(move) > 9:
            print("Please enter an integer between 1 and 9.")
            
        else:
            # checks if the space is taken
            is_taken = is_space_taken(int(move))
            
            # if the space is not taken, it places an X
            if is_taken == False:
                set_space(int(move), "X")
                break
            else:
                print("That spot is taken.")
    
    # if player 1 called "quit", it ends the game
    if game_over == True:
        break
    
    # prints the current grid
    print()
    print_grid()
    
    # checks for the winner
    winner = get_winner()
    if winner == "X":
        print("\r\nPlayer 1 wins!")
        game_over = True
        break
    elif winner == "Tie":
        print("\r\nThe game ended in a tie.")
        game_over = True
        break
    
    # creates a loop for player 2
    while True:
        # asks for input
        move = input("Player 2, please enter a grid number: ")
        
        # checks if the player wants to quit
        if move.lower() == "quit":
            game_over = True
            break
        
        # checks if the user input a valid digit
        elif move.isdigit() == False or int(move) < 1 or int(move) > 9:
            print("Please enter an integer between 1 and 9.")
            
        else:
            # checks if the space is taken
            is_taken = is_space_taken(int(move))
            
            # if the space is not taken, it places an O
            if is_taken == False:
                set_space(int(move), "O")
                break
            else:
                print("That spot is taken.")
    
    # if player 2 called "quit", it ends the game
    if game_over == True:
        break
    
    # prints the current grid
    print()
    print_grid()
    
    # checks for the winner
    winner = get_winner()
    if winner == "O":
        print("\r\nPlayer 2 wins!")
        game_over = True
        break

# thanks the players
print("\r\nThank you for playing!")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        