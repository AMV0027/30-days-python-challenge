import numpy as np

""" Initialize the board"""
def create_board():
    return np.zeros((3, 3), dtype=int)

""" Check if a move is valid"""
def is_valid_move(board, row, col):
    return board[row, col] == 0

""" Place a move on the board"""
def place_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row, col] = player
        return True
    return False

""" Check for a win"""
def check_win(board, player):
    """ Check rows, columns and diagonals"""
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    if board[0, 0] == board[1, 1] == board[2, 2] == player:
        return True
    if board[0, 2] == board[1, 1] == board[2, 0] == player:
        return True
    return False

""" Check for a draw"""
def check_draw(board):
    return np.all(board != 0)

""" Print the board"""
def print_board(board):
    for row in board:
        print(" ".join([str(x) if x != 0 else '.' for x in row]))
    print()

""" Minimax algorithm for AI move"""
def minimax(board, depth, is_maximizing):
    if check_win(board, 1):
        return -1
    if check_win(board, 2):
        return 1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row, col] == 0:
                    board[row, col] = 2
                    score = minimax(board, depth + 1, False)
                    board[row, col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row, col] == 0:
                    board[row, col] = 1
                    score = minimax(board, depth + 1, True)
                    board[row, col] = 0
                    best_score = min(score, best_score)
        return best_score

"""Find the best move for AI"""
def find_best_move(board):
    best_score = -float('inf')
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row, col] == 0:
                board[row, col] = 2
                score = minimax(board, 0, False)
                board[row, col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move
