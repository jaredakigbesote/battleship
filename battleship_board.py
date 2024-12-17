#imports 
import random
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
                    if ShipOverlaps(board, row, column, orientation, ShipLenght) == False:
                        #place ship
                        if orientation == 'H':
                            for i in range(column, column + ShipLenght):
                                board[row][i] = 'X'
                        else:
                            for i in range(row, row + ShipLenght):
                                board[i][column]  = 'X'
                    
                    
                    
                    break
        else:
            PlaceShips = True
            print('Place the ship with a length of ' + str(ShipLenght))
            row, column, orientation = user_input(PlaceShips)
            if check_ShipFit(ShipLenght, row, column, orientation,):
                if ShipOverlaps(board, row, column, orientation, ShipLenght) == False:
                    if orientation == 'H':
                        for i in range(column, column + ShipLenght):
                                board[row][i] = 'X'
                        else:
                            for i in range(row, row + ShipLenght):
                                board[i][column]  = 'X'
                        PrintBoard(PlayerBoard)
                        break


#checking df ships fit
def check_ShipFit(ShipLenght, row, column, orientation):
    if orientation == 'H':
        if column + ShipLenght > 11:
            return False
        else:
            return True
    else:
        if row + ShipLenght > 8:
            return False
        else: 
            return True

#overlapping
def check_ShipFit(ShipLenght, row, column, orientation):
    if orientation == 'H':
        for i in range(column, column + ShipLenght):
            if board[row][i] == 'X':
                return True
    else:
        for i in range(row, row, + ShipLenght):
            if board[i][column] == 'X':
                return True 
    return False
   
                    
            

