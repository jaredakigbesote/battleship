#imports 
from random import randint
#gameboards
Hiddenboard = [[' '] * 12 for x in range(12)]
Gameboard = [[' '] * 12 for x in range(12)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4 , 'F': 5 , 'G': 6 , 'H': 7 , 'I': 8 , 'J': 9 , 'K': 10 , 'L': 11}

#Functions
def PrintBoard(board):
    print('A B C D E F G H I J K L')
    print('=======================')
    rowNumber = 1
    for row in board:
        print("%d|%5|" % (rowNumber, "|" .join(row)))
        rowNumber += 1

def create_ships():
    for ship range (5):
    ShipRow, ShipColumn = randint(0, 11), randint(0, 11)
    while board[ShipRow][ShipColumn] == X

def get_shipLocation():
    pass

def count_shipHits():
    pass

create_ships()
turns = 15 
while turns > 0: