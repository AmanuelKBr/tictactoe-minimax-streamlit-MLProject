
from game_logic import check_winner, is_draw


def minimax(board, depth, is_maximizing):

    if check_winner(board,"O"):
        return 1

    if check_winner(board,"X"):
        return -1

    if is_draw(board):
        return 0


    if is_maximizing:

        best_score = -float("inf")

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(board, depth + 1, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score


    else:

        best_score = float("inf")

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(board, depth + 1, True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score



def best_move(board):

    best_score = -float("inf")

    move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board,0,False)

            board[i] = " "

            if score > best_score:

                best_score = score

                move = i

    return move
