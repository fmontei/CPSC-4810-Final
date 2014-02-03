import random

def display_instructions(blank_board):
    print("Greetings, human. We will pit our intellects against one another by playing" 
    "tic tac toe. Below is a board. Choose a number corresponding to the square"
    "to which you wish to assign a O or X.\n", blank_board)

def select_marker(piece):
    piece[0] = input("But first, select your marker (O or X): ").upper()
    while piece[0] not in ("O", "X"):
        piece[0] = input("Do not test me, human. Select either a O or X: ").upper()

    if piece[0] == "O":
        piece[1] = "X"
    else:
        piece[1] = "O"
    return piece

def determine_first_player():
    choice = input("\nTo see who goes first, pick heads or tails: ").lower()
    while choice not in ("heads", "tails"):
         choice = input("Do not test me. Pick heads or tails: ").lower()

    coin_toss = random.randint(0, 1)

    if coin_toss == 0:
        coin_toss = "heads"
    else:
        coin_toss = "tails"

    if choice == coin_toss:
        return 0
    else:
        return 1

def update_board(board, squares, choice, piece):
    squares.append(choice)
    board = board.replace(str(choice), piece)
    return board

def make_move(player_turn, board, squares, piece):
    if player_turn == 0:
        print("Your turn.")
        choice = int(input("Select a number (1 - 9): "))
        while choice not in range(1, 10):
            choice = int(input("Select a number (1 - 9): "))
        while choice in squares:
            choice = int(input("Obviously, that square is already occupied."
                               " Select another number: "))

        player_turn = 1
        board = update_board(board, squares, choice, piece)
    
    else:
        print("My turn.")
        computer_choice = random.randint(1, 10)
        while computer_choice in squares:
            computer_choice = random.randint(1, 10)

        player_turn = 0
        board = update_board(board, squares, computer_choice, piece)

    return board

def main():
    board = """
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    """
    squares = []
    piece = ["", ""]
        
    display_instructions(blank_board = board)
    select_marker(piece)
    first_move = determine_first_player()
    board = make_move(first_move, board, squares, piece[first_move])
    print(board)

    next_move = None
    if first_move == 0:
        next_move = 1
    else:
        next_move = 0
        
    while squares.count != 9:
        board = make_move(next_move, board, squares, piece[next_move])
        print(board)
        if next_move == 0:
            next_move = 1
        else:
            next_move = 0


    input("Press enter to exit.")
    

main()


