"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] is EMPTY:
                actions.add((row, col))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid action")

    new_board = deepcopy(board)
    
    new_board[action[0]][action[1]] = player(board)

    return new_board

def diagonals(board):
    return [[board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]]

def all_equal(board, winner=False):
    for row in board:
        if EMPTY not in row and row.count(row[0]) == len(row):
            if winner==True:
                if row[0] is X:
                    return X
                elif row[0] is O:
                    return O
            return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    options = [board, list(map(list, zip(*board))), diagonals(board)]
    
    for option in options:
        if all_equal(option):
            return all_equal(option, winner=True)
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if all_equal(board) or all_equal(list(map(list, zip(*board)))) or all_equal(diagonals(board)):
        return True

    filled = 0
    for row in board:
        if EMPTY not in row:
            filled += 1
    if filled == len(board):
        return True

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

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state():
        return 0,1

    best_value = (-math.inf if player(board) == X else math.inf)
    for action in actions(board):
        new_board = result(board, action)
        if player(board) == X:
            if min_value(new_board) > best_value:
                best_value = min_value(new_board)
                best_action = action
        elif player(board) == O:
            if max_value(new_board) < best_value:
                best_value = max_value(new_board)
                best_action = action
        
    return best_action