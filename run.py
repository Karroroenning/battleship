from random import randint

ships_length = [2,3,4]
player_guess_board = [[" "] * 8 for i in range(8)]
computer_guess_board = [[" "] * 8 for i in range(8)]
hidden_player_board = [[" "] * 8 for i in range(8)] 
hidden_computer_board = [[" "] * 8 for i in range(8)]



def menu():
    print(
    """
    __  ____ ___ ___ _    ____ ____ _  _ _ ___  ____
    |__] |__|  |   |  |    |___ [__  |__| | |__] [__
    |__] |  |  |   |  |___ |___ ___] |  | | |    ___]\n

    Press Enter to start

    """
        )       
    answer = input_val = input('')
    while True:
        if answer == '':
            #print_board(board)

    #"""
    #The gameboard. This code is copied by another coder (more info in my readme.md).
    #""""

def print_board(board):
    print("  A B C D E F G H")
    print("  ----------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


def create_ships(board):
    """
    Put 3 ships on the board. Horizontel or vertical. Player and computer puts ships that is 
    2, 3 or 3 ¤ long.
    """
    #Computer random puts out ships
    for ship_length in ships_length:
        while True:
            if board == computer_guess_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if ships_not_outside(ship_length, orientation, row, column):
                    if not_overlap(board, ship_length, row, column, orientation) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] == "¤"
                        else:
                            for i in range(row, row + ship_length):
                                board[column][i] == "¤"
                        break
            else:
                place_ship = True
                print('Deploy you ships to the board. Set out the length of' + str(ship_length))

                if ships_not_outside(ship_length, orientation, row, column):
                    if not_overlap(board, ship_length, row, column, orientation) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] == "¤"
                        else:
                            for i in range(row, row + ship_length):
                                board[column][i] == "¤"
                        break

def ships_not_outside(ship_length, orientation, row, column):
    """
    Check if the ships doesn't place outside the board.
    """
    if orientation == "H":
        if column + ship_length < 8:
            return True
        else: 
            return False
    else:
        if row + ship_length < 8:
            return True
        else:
            return False
    

def not_overlap(board, ship_length, row, column, orientation):
    """
    Check so the ships doesn't overlap the ships.
    """
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "¤"
                return True
    else: 
        for i in range(row, row + ship_length):
            if board[column][i] == "¤"
                return True
    return False


def get_ship_location():
    pass


def count_hit_ships():
    """
    Check if all ships are hit
    """
    pass

menu()