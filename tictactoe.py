"""
Tic Tac Toe Player
"""

import copy
import sys

X = "X"
O = "O"
EMPTY = None
memoization = {}

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    non_empty_count = sum(cell is not EMPTY for row in board for cell in row)
    if non_empty_count % 2 == 0:
        return X
    else:
        return O


def actions(board):
    actionsAvailable = set()
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == None:
                actionsAvailable.add((row, column))
    return actionsAvailable


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move: cell is already occupied.")
    if action[0] < 0 or action[1] < 0:
        raise Exception("Invalid move: Negative index")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    three_to_win_x = 0
    three_to_win_o = 0
    three_to_win_o_column = 0
    three_to_win_x_column = 0
    for row in range(len(board)):
        for column in range(len(board[row])):
            element = board[row][column]
            element_two = board[column][row]
            # Seccion de sumas
            if element_two != None and element_two == X:
                three_to_win_x_column += 1
            if element_two != None and element_two == O:
                three_to_win_o_column += 1
            if element != None and element == X:
                three_to_win_x += 1
            if element != None and element == O:
                three_to_win_o += 1
            # Seccion de calcular ganador
            if three_to_win_o == 3 or three_to_win_o_column == 3:
                return O
            if three_to_win_x == 3 or three_to_win_x_column == 3:
                return X
        three_to_win_x = 0
        three_to_win_o = 0
        three_to_win_o_column = 0
        three_to_win_x_column = 0

    cross = 0
    reverse = 2
    three_to_win_x_reverse = 0
    three_to_win_o_reverse = 0
    for i in range(len(board)):
        element = board[i][cross]
        element_two = board[i][reverse]

        if element != None and element == X:
            three_to_win_x += 1

        if element_two != None and element_two == X:
            three_to_win_x_reverse += 1

        if three_to_win_x == 3 or three_to_win_x_reverse == 3:
            return X

        if element != None and element == O:
            three_to_win_o += 1

        if element_two != None and element_two == O:
            three_to_win_o_reverse +=1

        if three_to_win_o == 3 or three_to_win_o_reverse == 3:
            return O
        cross += 1
        reverse -= 1


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != None or all(EMPTY not in row for row in board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    if terminal(board=board):
        return None
    if turn == X:
        best_action = None
        best_value = -sys.maxsize - 1
        for action in actions(board):
            value = min_value(result(board=board, action=action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action

    best_action = None
    best_value = sys.maxsize
    for action in actions(board=board):
        value = max_value(result(board=board, action=action))
        if value < best_value:
            best_action = action
            best_value = value
    return best_action


def min_value(board):
    board_key = tuple(tuple(row) for row in board)
    if board_key in memoization:
        return memoization[board_key]

    if terminal(board):
        memoization[board_key] = utility(board=board)
        return memoization[board_key]

    value = sys.maxsize
    for action in actions(board):
        board_to_calculate = result(board=board, action=action)
        value = min(value, max_value(board_to_calculate))
    memoization[board_key] = value
    return value


def max_value(board):
    board_key = tuple(tuple(row) for row in board)
    if board_key in memoization:
        return memoization[board_key]

    if terminal(board):
        memoization[board_key] = utility(board=board)
        return memoization[board_key]

    value = -sys.maxsize - 1
    for action in actions(board):
        board_to_calculate = result(board=board, action=action)
        value = max(value, min_value(board_to_calculate))

    memoization[board_key] = value
    return value
