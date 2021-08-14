import random


def printBoard(board: list):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def playGame():
    while True:
        if winner(board) or loser(board) is not True:
            position = int(input("Please enter a number from 1-9"))
            board[position] = user_team

            printBoard(board)

            opp_moves(board)
        else:
            break


def get_open_cells(board):
    open_cells: set = {cell for cell in range(1, 10) if board[cell] == " "}
    return open_cells


def loser(board):
    if board[1:4] or board[4:7] or board[7:10] or board[1:8:3] or board[2:9:3] or board[3:10:3] or board[1:10:4] or board[3:8:2] == [opp_team, opp_team, opp_team]:
        print("You Lose!")
        return True


def winner(board):
    if board[1:4] or board[4:7] or board[7:10] or board[1:8:3] or board[2:9:3] or board[3:10:3] or board[1:10:4] or board[3:8:2] == [user_team, user_team, user_team]:
        print("You Win!")
        return True


def opp_potential_win(board):
    for position in get_open_cells(board):
        if board[position] == loser(board):
            board[position] = opp_team
            printBoard(board)
            return True
        else:
            return False


def user_potential_win(board):
    for position in get_open_cells(board):
        if board[position] == winner(board):
            board[position] = user_team
            printBoard(board)
            return True
        else:
            return False


def placeMiddle(board):
    if 5 in get_open_cells(board):
        position = 5
        board[position] = opp_team
        printBoard(board)
        return True
    else:
        return False


def placeRandom(board):
    cell = random.randint(1, 10)

    if cell in get_open_cells(board):
        position = cell
        board[position] = opp_team
        printBoard(board)
        return True


def opp_moves(board):
    if opp_potential_win(board) == True:
        return

    elif user_potential_win(board) == True:
        return

    elif placeMiddle(board) == True:
        return

    elif placeRandom(board) == True:
        return


teams = ["O", "X"]
user_team = teams[1]
opp_team = teams[0]

board = [' '] * 10

playGame()

opp_moves(board)

# c2
