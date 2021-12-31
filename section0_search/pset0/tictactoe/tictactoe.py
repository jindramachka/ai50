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
    # Determine the number of cells each player has filled
    turn = {X: 0, O: 0}
    for row in board:
        for col in row:
            if col == X:
               turn[X] += 1
            elif col == O:
                turn[O] += 1

    # X always starts first
    if turn[X] == turn[O]:
        return X
    elif turn[X] > turn[O]:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    # If position (row, col) is empty, add it to possible actions
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] is EMPTY:
                actions.add((row, col))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Detemine if the action is valid
    if action not in actions(board):
        raise Exception("Not a valid action")

    # Make a deep copy of the board, so that the current board stays unmodified and the Minimax algorithm can consider many diffferent board states
    new_board = deepcopy(board)
    
    # Fill the cell determined by the action with current player
    new_board[action[0]][action[1]] = player(board)

    return new_board

def board_diagonals(board):
    """
    Returns the diagonals of the current board
    """
    return [[board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]]

def all_equal(board, winner=False):
    """
    1. winner = False: returns True if any player has filled all cells in a any row/column/diagonal, otherwise False
    2. winner = True: returns the player that has filled all cells in a any row/column/diagonal, if any of the players managed
    """
    for row in board:
        # There is a winner if all of the cells in row/column/diagonal are filled by the same value and are not empty
        if EMPTY not in row and row.count(row[0]) == len(row):

            # Return the winner only if the caller function wants to return the winner
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
    # List of board rows, board columns and board diagonals
    options = [board, list(map(list, zip(*board))), board_diagonals(board)]
    
    # Get the winner of the current board
    for option in options:
        if all_equal(option):
            return all_equal(option, winner=True)
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if any player ha filled all cells in any row/column/diagonal
    if all_equal(board) or all_equal(list(map(list, zip(*board)))) or all_equal(board_diagonals(board)):
        return True

    # Check if the board is completely filled
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
    """
    Recursively explores all the possible outcomes of the board and returns the maximum value of the board if the opponent always plays for the minimum value
    """
    # If either the algorithm predicted all the moves up until a terminal state, or if the game has gone into a possible terminal state, return the final value
    if terminal(board):
        return utility(board)

    v = -math.inf # The algorithm can always get a better value than the default -infinity

    # Check each possible action and return the best possible value
    for action in actions(board):
        # Update the best value if the minimum value of the board that results form the action is better than the current best value
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    """
    Recursively explores all the possible outcomes of the board and returns the minimum value of the board if the opponent always plays for the maximum value
    """
    # If either the algorithm predicted all the moves up until a terminal state, or if the game has gone into a possible terminal state, return the final value
    if terminal(board):
        return utility(board)

    v = math.inf # The algorithm can always get a better value than the default +infinity

    # Check each possible action and return the best possible value
    for action in actions(board):
        # Update the best value if the minimum value of the board that results form the action is better than the current best value
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Optimization for the case if the computer starts first
    if board == initial_state():
        return 0,1

    # The algorithm is always find a better value than the default ones: -infinity for X, +infinity for O
    best_value = (-math.inf if player(board) == X else math.inf) 

    # Check the best possible value for each possible action
    for action in actions(board):
        new_board = result(board, action) # The board that results from the action

        # X: Find the action that results in maximum possible value if O always plays for the minimum possible value
        if player(board) == X:
            # If the value of the current action is better than the value of the action checked before, update the best action and the best value
            if min_value(new_board) > best_value:
                best_value = min_value(new_board)
                best_action = action

        # O: FInd the action that results in minimum possible value if X always plays for the maximum possible value
        elif player(board) == O:
            # If the value of the current action is better than the value of the action checked before, update the best action and the best value
            if max_value(new_board) < best_value:
                best_value = max_value(new_board)
                best_action = action
        
    return best_action