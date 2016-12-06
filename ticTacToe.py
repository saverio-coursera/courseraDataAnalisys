__author__ = 'saverio'

import numpy as np
import random
import time


def create_board():
    return (np.zeros((3, 3)))


def place(board, player, position):
    if board[position[0], position[1]] == 0:
        board[position[0], position[1]] = player


def possibilities(board):
    nz = np.where(board == 0)
    result = []
    for t in range(len(nz[0])):
        result.append((nz[0][t], nz[1][t],))
    return (result)


def random_place(board, player):
    m = random.choice(possibilities(board))
    place(board, player, m)


def row_win(board, player):
    for r in range(0, 3):
        myrow = board[r, :]
        if sum(myrow == player) == 3:
            return (True)
    return (False)


def col_win(board, player):
    for c in range(0, 3):
        mycol = board[:, c]
        if sum(mycol == player) == 3:
            return (True)
    return (False)


def diag_win(board, player):
    myD1 = np.array([board[0, 0], board[1, 1], board[2, 2]])
    if sum(myD1 == player) == 3:
        return (True)
    myD2 = np.array([board[0, 2], board[1, 1], board[2, 0]])
    if sum(myD2 == player) == 3:
        return (True)
    return (False)


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0):
        winner = -1
    return winner


def play_game():
    board = create_board()
    while evaluate(board) == 0:
        for p in [1,2]:
            random_place(board, p)
            e = evaluate(board)
            if e != 0:
                return (e)
    return (-1)



scores=[0,0]
for g in range(0, 100):
    winner=play_game()
    if winner==1:
        scores[0]+=1
    if winner==2:
        scores[1]+=1

print(scores)
