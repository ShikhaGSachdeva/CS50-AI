"""
Tic Tac Toe Player
"""

import copy
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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))
    
    return possible_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    
    row, col = action
    
    new_board = copy.deepcopy(board)
    new_board[row][col] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] != EMPTY:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != EMPTY:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != EMPTY:
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0] != EMPTY:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != EMPTY:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != EMPTY:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winner_exists = winner(board) is not None
    no_empty_cells = all(cell != EMPTY for row in board for cell in row)  
    if winner_exists or no_empty_cells:
        return True
    return False

    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    best = float('-inf')
    for action in actions(board):
        best = max(best, min_value(result(board, action)))
    return best


def min_value(board):
    if terminal(board):
        return utility(board)
    best = float('inf')
    for action in actions(board):
        best = min(best, max_value(result(board, action)))
    return best


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        best_value = float('-inf')
        best_action = None
        
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
    else:
        best_value = float('inf')
        best_action = None
        
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
 
    return best_action
