def check_winner(board, player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw(board):
    return all(cell != " " for cell in board)
