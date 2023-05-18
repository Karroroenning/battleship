import random

ships_length = [2, 3, 4]
player_guess_board = [[' '] * 8 for i in range(8)]
computer_guess_board = [[' '] * 8 for i in range(8)]
hidden_player_board = [[' '] * 8 for i in range(8)]
hidden_computer_board = [[' '] * 8 for i in range(8)]
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    }


def menu():
    print(
        """
    __  ____ ___ ___ _    ____ ____ _  _ _ ___  ____
    |__] |__|  |   |  |    |___ [__  |__| | |__] [__
    |__] |  |  |   |  |___ |___ ___] |  | | |    ___]


    """
    )


def print_board(board):
    print('  A B C D E F G H')
    print(' -----------------')
    row_number = 1
    for row in board:
        print('%d|%s|' % (row_number, '|'.join(row)))
        row_number += 1


def create_ships(board):
    """
    Put 3 ships on the board.
    """

    # Computer random puts out ships

    for ship_length in ships_length:
        while True:
            if board == computer_guess_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if ships_not_outside(ship_length, row, column, orientation):
                    if not_overlap(board, row, column, orientation,
                                   ship_length) is False:
                        if orientation == 'H':
                            for i in range(column, column + ship_length):
                                board[row][i] = 'X'
                        else:
                            for i in range(row, row + ship_length):
                                board[column][i] == 'X'
                        break
            else:
                place_ship = True
                print('Deploy you ships to the board.')
                print('Set out the length of ' + str(ship_length))
                (row, column, orientation) = \
                    place_ship_location(place_ship)
                if ships_not_outside(ship_length, row, column, orientation):
                    if not_overlap(board, row, column, orientation,
                                   ship_length) is False:
                        if orientation == 'H':
                            for i in range(column, column+ship_length):
                                board[row][i] = 'X'
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = 'X'
                        print_board(player_guess_board)
                        break


def ships_not_outside(
    ship_length,
    row,
    column,
    orientation,
):
    """
    Check if the ships doesn't place outside the board.
    """

    if orientation == 'H':
        if column + ship_length > 8:
            return False
        else:
            return True
    else:
        if row + ship_length > 8:
            return False
        else:
            return True


def not_overlap(
    board,
    row,
    column,
    orientation,
    ship_length,
):
    """
    Check so the ships doesn't overlap the ships.
    """

    if orientation == 'H':
        for i in range(column, column + ship_length):
            if board[row][i] == 'X':
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == 'X':
                return True
    return False


def place_ship_location(place_ship):
    """
    Player places the ships on the gameboard.
    """

    if place_ship is True:
        while True:
            try:
                orientation = input('Enter orientation (H or V):\n '
                                    ).upper()
                if orientation == 'H' or orientation == 'V':
                    break
            except TypeError:
                print('Enter a valid oriantation, H or V')
        while True:
            try:
                row = input('Enter the row 1-8 of the ship:\n ')
                if row in '12345678':
                    row = int(row) - 1
                    break
            except TypeError:
                print('Enter a valid number between 1-8')
        while True:
            try:
                column = input('Enter the column A-H of the ship:\n '
                               ).upper()
                if column in 'ABCDEFGH':
                    column = letters_to_numbers[column]
                    break
            except TypeError:
                print('Enter a valid letter between A-H')
        return (row, column, orientation)
    else:
        while True:
            try:
                row = \
                    input('Choose a number between 1-8 in the row:\n'
                          )
                if row in '12345678':
                    row = int(row) - 1
                    break
            except TypeError:
                print('Choose a valid number between 1-8')
        while True:
            try:
                column = input('Choose a letter in the column:\n '
                               ).upper()
                if column in 'ABCDEFGH':
                    column = letters_to_numbers[column]
                    break
            except TypeError:
                print('Choose a valid letter between A-H')
        return (row, column)


def count_hit_ships(board):
    """
    Check if all ships are hit
    """

    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def turn(board):
    """
    if the player and computer hit or miss the boats.
    """

    if board == hidden_player_board:
        (row, column) = place_ship_location(hidden_player_board)
        if board[row][column] == '-':
            turn(board)
        elif board[row][column] == 'X':
            turn(board)
        elif computer_guess_board[row][column] == 'X':
            board[row][column] = 'X'
        else:
            board[row][column] = '-'
    else:
        (row, column) = (random.randint(0, 7), random.randint(0, 7))
        if board[row][column] == '-':
            turn(board)
        elif board[row][column] == 'X':
            turn(board)
        elif player_guess_board[row][column] == 'X':
            board[row][column] = 'X'
        else:
            board[row][column] = '-'


menu()
create_ships(computer_guess_board)
create_ships(player_guess_board)
print_board(player_guess_board)

while True:

    # player turn

    while True:
        print('Guess a battleship location')
        print_board(hidden_player_board)
        turn(hidden_player_board)
        break
    if count_hit_ships(hidden_player_board) == 9:
        print('BOOM, You Win!')
        break

    # computer turn

    while True:
        turn(hidden_computer_board)
        break
    print_board(hidden_computer_board)
    if count_hit_ships(hidden_computer_board) == 9:
        print('BOOM, You lose!')
        break
