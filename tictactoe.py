# this is a python script to create a tic tac toe game.


def main():

     # setup game

    # alternate turns

    # check if win or end

    # quit and show the board

 

    print_instruction()

 

    board = []

    for i in range(9):

        board.append(-1)
 

    win = False

    move = 0

    while not win:

 

        # print board

        print_board(board)

        print “Turn number “ + str(move+1)

        if move % 2 == 0:

            turn = ‘X’

        else:

            turn = ‘O’

 
        # get user input

        user = get_input(turn)

        while board[user] != -1:
            print “Invalid move! Cell already taken. Please try again.\n”

            user = get_input(tun)

        board[user] = 1 if turn == ‘X’ else 0
        # advance move and check for end game

        move += 1

        if move > 4:

            winner = check_win(board)

            if winner != -1:

                out = “The winner is “

                out += “X” if winner == 1 else “O”

                out += “ ☺”
		              quit_game(board,out)

            elif move == 9:
		quit_game(board,”No winner :(”))

