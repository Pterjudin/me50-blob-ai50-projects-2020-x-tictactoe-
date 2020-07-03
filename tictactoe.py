"""
Tic Tac Toe Player
"""

import math
import copy
import numpy as np

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

    NB:- There are players X and Y for the Tic Tac Toe game.
    
    * X gets the first move. The players alternate subsequently. 
    * If a terminal board is provided as input then the game is over.        
    """
    count = 0  # If the final value for count is even then the next player is O else X.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                count += 1

    if count % 2 == 0:
        return 'O'
    elif count % 2 == 1:
        return 'X'
    else: return count          


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                actions.append((i,j))
    return actions

 


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    allowed_actions = actions(board)
    
    if action not in allowed_actions:
        raise Exception("Action is Not Allowed")
    
    next_player = player(board)

    if next_player == 'X' or 'O':
        board_copy[action[0]][action[1]] = next_player    

    return board_copy

def checkRows(board):
    """ 
    This functon checks the row for a winner
    """
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None

def checkDiagonals(board):
    """ 
    This functon checks the diagonals for a winner
    """
    if len(set([board[i][i] for i in range(len(board))])) == 1: # (0,0) (1,1) (2,2)
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
       #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                return False

    return True                
           


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if not terminal(board):
        return False

    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1 

    return 0    



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if current_player == "X":
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))    
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))    
            if k < v:
                v = k
                best_move = action
    return best_move

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
    

 