# imports
import random
# ship lenght
Length_of_ships = [2, 2, 3, 3, 4, 5]
# gameboards
player_board = [[' '] * 12 for x in range(12)]
computer_board = [[' '] * 12 for x in range(12)]
player_guess_board = [[' '] * 12 for x in range(12)]
computer_guess_board = [[' '] * 12 for x in range(12)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11}

# Functions


def print_board(board):
    print('A B C D E F G H I J K L')
    print('=======================')
    row_number = 1
    for row in board:
        print(F'{row_number}-')
        row_number += 1

# place ships


def place_ships(board):
    for ship_lenght in Length_of_ships:
        while True:
            if board == computer_board:
                orientation, row, column = random.choice(["h", "v"]), random.randint(1, 12), random.randint(1, 12)
                if check_ship_fit(ship_lenght, row, column, orientation):
                    # overlaps
                    if ship_overlaps(ship_lenght, board, row, column, orientation) is False:
                        # place ship
                        if orientation == "h":
                            for i in range(column, column + ship_lenght):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_lenght):
                                board[i][column] = "X"

                        break
        else:
            place_ships = True
            print('Place the ship with a length of ' + str(ship_lenght))
            row, column, orientation = user_input(place_ships)
            if check_ship_fit(ship_lenght, row, column, orientation):
                # ship overlaps
                if ship_overlaps(ship_lenght, board, row, column, orientation) is False:
                    if orientation == "h":
                        # place ship
                        for i in range(column, column + ship_lenght):
                            board[row][i] = "X"
                    else:
                        for i in range(row, row + ship_lenght):
                            board[i][column] = "X"
                    print_board(player_board)
                    break
            

# checking df ships fit
def check_ship_fit(ship_lenght, row, column, orientation):
    if orientation == "h":
        if column + ship_lenght > 12:
            return False
        else:
            return True
    else:
        if row + ship_lenght > 12:
            return False
        else:
            return True

# overlapping


def ship_overlaps(ship_lenght, board, row, column, orientation):
    if orientation == "h":
        for i in range(column, column + ship_lenght):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row, + ship_lenght):
            if board[i][column] == "X":
                return True
    return False
# user input for ships


def user_input(place_ships):
    if place_ships is True:
        while True:
            try:
                orientation = input("Enter orientation (h or v):").upper()
                if orientation == "h" or orientation == "v":
                    break
            except TypeError:
                print('Enter a valid orientation h or v')
        while True:
            try:
                row = input("Enter the row 1-12 for ship: ")
                if row in '123456789101112':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-12')
        while True:
            try:
                column = input("Enter the column of the ship:").upper()
                if column in 'ABCDEFGHIJKL':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print("Enter a valid letter between A-L")
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter a row 1-12 of ships:")
                if row in '123456789101112':
                    row = int(row) - 1
                    break
            except ValueError:
                print('enter a valid letter betwwen 1-12')
        while True:
            try:
                column = input("Enter the column of the ship:").upper()
                if column in 'ABCDEFGHIJKL':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-L')
        return row, column

# check hits


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column in row:
                if column == "X":
                    count += 1
        return count


# Turns
def turn(board):
    if board == player_guess_board:
        row, column = user_input(player_guess_board)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif computer_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(1, 12), random.randint(1, 12)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif player_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"


print_board(computer_board)
print('run1')
place_ships(computer_board)
print('run2')
print_board(player_board)
print('run3')
place_ships(player_board)
print('run4')

while True:
    # player
    while True:
        print('Guess a Battleship location')
        print_board(player_guess_board)
        turn(player_guess_board)
        break
    if count_hit_ships(player_guess_board) == 19:
        print("You win")
        break
    # computer
    while True:
        turn(computer_guess_board)
        break
    print_board(computer_guess_board)
    if count_hit_ships(computer_guess_board) == 19:
        print("You lose")
        break
