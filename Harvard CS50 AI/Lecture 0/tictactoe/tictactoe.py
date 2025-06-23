"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None
GameOver = False
FirstPlayer = ""

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    numofx = 0
    numofy = 0
    for i in board:
        for j in i:
            if j == X:
                numofx+=1
            if j == O:
                numofy+=1
    if numofx <= numofy:
        return X
    else:
        return O


def actions(board):
    PossibleActions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                PossibleActions.append((i,j))
    return PossibleActions


def result(board, action):
    print(action)
    ResultBoard = [i[:] for i in board]
    ResultBoard[action[0]][action[1]] = player(board)
    return ResultBoard


def winner(board):
    if terminal(board) == True:
        TerminalBoards = [
                         #Rows
                         [board[0][0], board[0][1], board[0][2]],
                         [board[1][0], board[1][1], board[1][2]],
                         [board[2][0], board[2][1], board[2][2]],
                         #Colums
                         [board[0][0], board[1][0], board[2][0]],
                         [board[0][1], board[1][1], board[2][1]],
                         [board[0][2], board[1][2], board[2][2]],
                         #Diagonals
                         [board[0][0], board[1][1], board[2][2]],
                         [board[0][2], board[1][1], board[2][0]]
                         ]
    
        for i in TerminalBoards:
            if X == i[0] == i[1] == i[2]:
                return X
            elif O == i[0] == i[1] == i[2]:
                return O
            

def terminal(board):
    global GameOver
    TerminalBoards = [
                     #Rows
                     [board[0][0], board[0][1], board[0][2]],
                     [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]],
                     #Colums
                     [board[0][0], board[1][0], board[2][0]],
                     [board[0][1], board[1][1], board[2][1]],
                     [board[0][2], board[1][2], board[2][2]],
                     #Diagonals
                     [board[0][0], board[1][1], board[2][2]],
                     [board[0][2], board[1][1], board[2][0]]
                     ]
    
    for i in TerminalBoards:
        if X == i[0] == i[1] == i[2]:
            GameOver = True
            return True
        elif O == i[0] == i[1] == i[2]:
            GameOver = True
            return True
    if all(j is not None for i in board for j in i):
            GameOver = True
            return True
    else:
        GameOver = False
        return False

    raise NotImplementedError


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def MaxValue(state):
    if terminal(state):
        return utility(state), None
    v = -math.inf
    BAct = None
    for action in actions(state):
        m,_ = MinValue(result(state, action))
        if m > v:
            print("Found new V : {}".format(v))
            v = m
            BAct = action
    return v, BAct

def MinValue(state):
    if terminal(state):
        return utility(state), None
    v = math.inf
    BAct = None
    for action in actions(state):
        m,_ = MaxValue(result(state, action))
        if m < v:
            print("Found new V : {}".format(v))
            v = m
            BAct = action
    return v, BAct

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player = player(board)
    if current_player == X:
        _,ACT = MaxValue(board)
    elif current_player == O:
        _,ACT = MinValue(board)

    return ACT

    raise NotImplementedError
