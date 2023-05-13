#import random

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
            rungame()


#class Gameboard:
    #"""
    #The gameboard. This code is copied by another coder (more info in my readme.md).
    #"""
    #def __init__(self, board):
        #self.board = board

    #def get_letters_to_numbers():
        #letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        #return letters_to_numbers

    #def print_board(self):
        #print("  A B C D E F G H")
        #print("  ---------------")
        #row_number = 1
        #for row in self.board:
            #print("%d|%s|" % (row_number, "|".join(row)))
            #row_number += 1

#class Battleship:
    #def __init__(self, board):

    #def create_ships(self):
        #"""
        #The player set there ships location to the board
        #"""

    #def get_ships_location(self):
        #"""
        #Ask the player wich colums and location they want to put there bomb to sink the computers ships
        #"""

    #def count_hit_ships(self):
        #"""
        #Count everytime you hit a ship
        #"""


def rungame():
    """
    Start the game
    """
    print('Welcome')


rungame()
menu()