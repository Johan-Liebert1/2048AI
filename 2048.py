# TEST FILE
from termcolor import colored
import numpy as np

def newGrid():
    return np.array([
            [4,0,8,8,0,4],
            [0,0,0,0,0,0],
            [16,0,0,0,0,16],
            [16,0,0,0,0,16],
            [0,0,0,0,0,0],
            [2,0,8,8,0,2],
        ])
board = newGrid()

def shiftRight(board):
    # newBoard = newGrid()
    for row in board:
        for i in range(len(row) - 1, 0, -1): # 0 is excluded
            if row[i] == row[i - 1]:
                row[i] = row[i] * 2
                row[i-1] = 0
        slideRight(board)


def slideRight(board):
    for row in board:
        for i in range(len(board) - 1):
            if row[i] != 0 and row[i + 1] == 0:
                row[i + 1] = row[i]
                row[i] = 0


def slideLeft(board):
    for row in board:
        for i in range(len(board) - 1):
            if row[i + 1] != 0 and row[i] == 0:
                row[i] = row[i + 1]
                row[i + 1] = 0

def shiftLeft(board):
    shiftRight(board)

    for _ in range(len(board)):
        slideLeft(board)


def shiftDown(board):
    board = board.T

    shiftRight(board)
    board = board.T


def shiftUp(board):
    board = board.T

    shiftLeft(board)
    board = board.T


def print_board_numbers(board):
    string = ''
    for i in range(len(board)):
        string += '\n\n'
        for j in range(len(board)):
            color = 'green' if board[i][j] != 0 else 'white'

            string += colored(board[i][j], color) + "    "
    print(string, "\n\n")


print_board_numbers(board)
# shiftRight(board)
# print_board_numbers(board)
# shiftLeft(board)
shiftUp(board)
print_board_numbers(board)

# for row in board:
#     row = row[::-1]
#     print(row)

# print_board_numbers(board)

