import random


def printBoard(board: list):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


# the reason that opp_potential win doesn't work is because i coded it to block if user_team showed up, but I used the opp_team character, so OOX wouldn't register.

def playGame():
    while True:
        win = winner(user_team)
        lose = winner(opp_team)

        # if winner() or loser() is not True:

        if (win is not True) and (lose is not True):
            position = int(input("Please enter a number from 1-9: "))
            board[position] = user_team

            printBoard(board)
            print("===========================")
            print(get_open_cells(board))

            opp_moves(board)
            print(get_open_cells(board))

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

# def loser():
# v_rows = rows(board)
# if [opp_team, opp_team, opp_team] in v_rows:
# return True
# else:
# return False


def winner(team):
    v_rows = rows(board)
    if [team, team, team] in v_rows:
        return True
    else:
        return False


# create one function because it's repetitive
# letter becomes parameter

def potential_win(board, team, testing):
    move = False
    open_pos = get_open_cells(board)
    p = 1
    row = rows(board)

    for oc in open_pos:
        board[oc] = testing

        for i in row:
            if i == [testing, testing, testing]:
                p = oc
                move = True
                break
        # if (board[position] := testing) == rows(board):
        # board[position] = team
        # printBoard(board)
        # return True
        # else:
        # return False
        if move == False:
            board[p] = team

    return move


# def user_potential_win(board):
# for position in get_open_cells(board):
# if (board[position] == user_team) == rows(board):
# board[position] = user_team
# printBoard(board)
# return True
# else:
# return False


def placeMiddle(board):
    if 5 in get_open_cells(board):
        position = 5
        board[position] = opp_team
        printBoard(board)
        return True
    else:
        return False


def placeRandom(board):
    print(get_open_cells(board))
    cell = random.choice(get_open_cells(board))

    if cell in get_open_cells(board):
        position = cell
        board[position] = opp_team
        printBoard(board)
        return True


def opp_moves(board):
    # opp won
    if potential_win(board, opp_team, opp_team) == True:
        return
    # block user win
    elif potential_win(board, opp_team, user_team) == True:
        return

    elif placeMiddle(board) == True:
        return

    elif placeRandom(board) == True:
        return


# teams = ["O", "X"]

# user_team = teams[1]
# opp_team = teams[0]


teams = ["O", "X"]

user_number = (int(input("Please enter 0 to choose X or 1 to choose O")))

user_team = teams[user_number]
opp_team = teams[(not user_number)]

board = [' '] * 10

playGame()

print("game over")
