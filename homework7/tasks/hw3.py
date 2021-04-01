"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
import itertools
from typing import List

import numpy as np


def check_unfinished(board):
    flat_board = [*itertools.chain.from_iterable(board)]
    return "-" in flat_board


def check_rows(board):
    for row in board:
        if len(set(row)) == 1:
            return row.pop()


def check_cols(board):
    return check_rows(np.transpose(board).tolist())


def check_diagonals(board):
    return (
        len(set(np.diagonal(board))) == 1 or len(set(np.fliplr(board).diagonal())) == 1
    )


def tic_tac_toe_checker(board: List[List]) -> str:

    if check_rows(board):
        return f"{check_rows(board)} wins!"

    elif check_cols(board):
        return f"{check_cols(board)} wins!"

    elif check_diagonals(board):
        return f"{board[1][1]} wins!"

    elif check_unfinished(board):
        return "unfinished"

    return "draw!"
