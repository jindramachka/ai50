"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # if terminal(board) == True

    turn = {X: 0, O: 0}
    for row in board:
        for col in row:
            if col == X:
               turn[X] += 1
            elif col == O:
                turn[O] += 1

    if turn[X] == turn[O]:
        return X
    elif turn[X] > turn[O]:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in board:
        for col in row:
            if col is EMPTY:
                actions.append((row, col))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    


    raise NotImplementedError

def all_equal(board):
    for row in board:
        if row.count(row[0]) == len(row):
            return True
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    diagonals = [[board[0, 0], board[1, 1], board[2, 2]],
                 [board[0, 2], board[1, 1], board[2, 0]]]

    if all_equal(board) or all_equal(board.T) or all_equal(diagonals):
        return True
    
    # for row in board:
    #     if row.count(row[0]) == len(row):
    #         return True

    # for row in board.T:
    #     if row.count(row[0] == len(row)):
    #         return True

    # if diagonals[0].count(diagonals[0][0]) == len(diagonals[0]) or diagonals[1].count(diagonals[1][0]) == len(diagonals[1]):
    #     return True

    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

print(initial_state())