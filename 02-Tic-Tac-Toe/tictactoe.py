# chyk2468
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

    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {
        (i, j)
        for i in range(3)
        for j in range(3)
        if board[i][j] == EMPTY
    }


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise ValueError("Action cannot be None")

    try:
        i, j = action
    except (TypeError, ValueError):
        raise ValueError("Action must be a 2-tuple (i, j)")

    if not (0 <= i < 3 and 0 <= j < 3):
        raise IndexError("Action coordinates out of bounds")

    if board[i][j] != EMPTY:
        raise ValueError("Invalid action: cell is already occupied")

    new_board = [row.copy() for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] is not None and row[0] == row[1] == row[2]:
            return row[0]

    # Check columns
    for col in range(3):
        if (board[0][col] is not None and
                board[0][col] == board[1][col] == board[2][col]):
            return board[0][col]

    # Check main diagonal
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # Check anti-diagonal
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    # If any cell is empty, the game is still in progress
    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_val = -math.inf
        best_move = None
        alpha = -math.inf
        beta = math.inf

        for action in actions(board):
            val = min_value(result(board, action), alpha, beta)
            if val > best_val:
                best_val = val
                best_move = action
            alpha = max(alpha, best_val)
            if best_val == 1:
                break
        return best_move

    else:
        best_val = math.inf
        best_move = None
        alpha = -math.inf
        beta = math.inf

        for action in actions(board):
            val = max_value(result(board, action), alpha, beta)
            if val < best_val:
                best_val = val
                best_move = action
            beta = min(beta, best_val)
            if best_val == -1:
                break
        return best_move


def max_value(board, alpha, beta):
    """
    Helper function for Minimax: returns maximum utility value for X.
    """
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def min_value(board, alpha, beta):
    """
    Helper function for Minimax: returns minimum utility value for O.
    """
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
