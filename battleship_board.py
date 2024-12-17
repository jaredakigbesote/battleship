#imports 
from random import randint
#ship lenght
Length_ofShips = [2, 2, 3, 3, 4, 5]
#gameboards
PlayerBoard = [[' '] * 12 for x in range(12)]
ComputerBoard = [[' '] * 12 for x in range(12)]
Player_GuessBoard = [[' '] * 12 for x in range(12)]
Computer_GuessBoard = [[' '] * 12 for x in range(12)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4 , 'F': 5 , 'G': 6 , 'H': 7 , 'I': 8 , 'J': 9 , 'K': 10 , 'L': 11}

#Functions
def PrintBoard(board):
    print('A B C D E F G H I J K L')
    print('=======================')
    rowNumber = 1
    for row in board:
        print("%d|%5|" % (rowNumber, "|" .join(row)))
        rowNumber += 1
#place ships
def PlaceShips(board):
    for ShipLenght in Length_ofShips:
        while True:
            if board == ComputerBoard:
                orientation, row, column = random.choice(['h', 'V']), random.randint(0,11), random.randint(0,11)
                if check_ShipFit(ShipLenght, row, column, orientation):
                    if ShipOverlaps(board, row, column, orientation, ShipLenght) == False
                    #place ship
                    if orientation == 'H':
                        for i in range(column, column + ShipLenght):
                            board[row][i] = 'X'
                    else: 
                        for i in range(row, row + ShipLenght)
                        board[i][column] = 'X'
                    
                    break
        else:
            PlaceShips = True
            print('Place the ship with a length of ' + str(ShipLenght))
            row, column, orientation = user_input(PlaceShips)
            if check_ShipFit(ShipLenght, row, column, orientation,):
                if ShipOverlaps(board, row, column, orientation):
            

#ship location
def get_shipLocation():
    row = input('Enter a ship row').upper()
    while row not in '1234567891011':
        print('Please enter a valid row')
        row = input('Please enter a ship row')
        column = input('Please enter a ship column').upper()
    while column not in 'ABCDEFGHIJKL':
        print('Please enter a valid column')
        column = input('please enter a ship colunm').upper()
    return int(row) - 1, letters_ToNumbers(column)

def count_shipHits(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
                return count

create_ships(Hiddenboard)
turns = 15
PrintBoard(Hiddenboard)
PrintBoard(Gameboard)
while turns > 0: