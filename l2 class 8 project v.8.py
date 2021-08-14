import random


def printBoard(board: list):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


# lose is not necessary, create win and draw with an initial value (draw is False)

def playGame():
    while True:
        win = get_winner(user_team)
        lose = get_winner(opp_team)
        draw = tie()

        if (win is not True) and (lose is not True) and (draw is not True):
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

        elif draw is True:
            print("Draw!")
            break

        else:
            break


def get_open_cells(board):
    open_cells: list = [cell for cell in range(1, 10) if board[cell] == " "]
    return open_cells


def rows(board):
    row = [board[1:4], board[4:7], board[7:10], board[1:8:3], board[2:9:3], board[3:10:3], board[1:10:4], board[3:8:2]]

    return row


def get_winner(team):
    v_rows = rows(board)
    if [team, team, team] in v_rows:
        return True
    else:
        return False


def tie():
    if get_open_cells(board) == []:
        return True
    else:
        return False


def potential_win(board, team, testing):
    move = False
    open_pos = get_open_cells(board)

    for oc in open_pos:
        board[oc] = testing
        row = rows(board)

        for i in row:

            if i == [testing, testing, testing]:
                move = True
                board[oc] = team
                printBoard(board)
                break
            else:
                board[oc] = " "

        if move == True:
            break

    return move


def placeMiddle(board):
    if 5 in get_open_cells(board):
        position = 5
        board[position] = opp_team
        printBoard(board)
        return True
    else:
        return False


# add a return false

def placeRandom(board):
    while tie() == False:
        cell = random.choice(get_open_cells(board))

        if cell in get_open_cells(board):
            position = cell
            board[position] = opp_team
            printBoard(board)
            return True
        else:
            return False


def opp_moves(board):
    if potential_win(board, opp_team, opp_team) == True:
        return

    elif potential_win(board, opp_team, user_team) == True:
        return

    elif placeMiddle(board) == True:
        return

    elif placeRandom(board) == True:
        return


while True:
    play_again = str(input("Would you like to play Tic-Tac_Toe? Type 'yes' to play again, type 'no' to quit: "))
    teams = ["O", "X"]

    if play_again == "no":
        break

    if play_again == "yes":
        user_number = (int(input("Please enter 0 to choose X or 1 to choose O: ")))

        user_team = teams[user_number]
        opp_team = teams[(not user_number)]

        board = [' '] * 10

        playGame()
        print("game over")

# c9

