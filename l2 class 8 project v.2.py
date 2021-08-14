import random


def printBoard(board: list):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def playGame():
    while True:
        win = winner()
        lose = loser()

        # if winner() or loser() is not True:

        if (win is not True) and (lose is not True):
            position = int(input("Please enter a number from 1-9: "))
            board[position] = user_team

            printBoard(board)
            print("===========================")

            opp_moves(board)

        elif win is True:
            print("You Win!")
            break

        elif lose is True:
            print("You Lose!")
            break

        else:
            break


def get_open_cells(board):
    open_set: set = {cell for cell in range(1, 10) if board[cell] == " "}
    open_cells = list(open_set)
    return open_cells


def rows(board):
    row = [board[1:4], board[4:7], board[7:10], board[1:8:3], board[2:9:3], board[3:10:3], board[1:10:4], board[3:8:2]]

    return row

# can just do winner
# put a tie 

def loser():
    v_rows = rows(board)
    if [opp_team, opp_team, opp_team] in v_rows:
        return True
    else:
        return False


def winner():
    v_rows = rows(board)
    if [user_team, user_team, user_team] in v_rows:
        return True
    else:
        return False

# create one function because it's repetitive
# letter becomes parameter

def opp_potential_win(board):
    for position in get_open_cells(board):
        if (board[position] == opp_team) == rows(board):
            board[position] = opp_team
            printBoard(board)
            return True
        else:
            return False


def user_potential_win(board):
    for position in get_open_cells(board):
        if (board[position] == user_team) == rows(board):
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
    cell = random.choice(get_open_cells(board))

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
# row = board[1:4] or board[4:7] or board[7:10] or board[1:8:3] or board[2:9:3] or board[3:10:3] or board[1:10:4] or board[3:8:2]

playGame()

print("game over")

# opp_moves(board)

# c3
