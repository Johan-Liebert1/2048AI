# TEST FILE
from termcolor import colored
import numpy as np

def tempGrid():
    return np.array([[0]*6 for _ in range(6)])

def newGrid():
    return np.array([
            [4,0,8,8,0,4],
            [4,2,2,2,2,0],
            [16,0,0,0,0,16],
            [16,0,0,0,0,16],
            [0,0,0,0,0,0],
            [2,0,8,8,0,2],
        ])
board = newGrid()

def shiftRight(board):
    board = slideRight(board)
    print(colored("After first slide right", 'red'))
    print_board_numbers(board)
    
    for row in board:
        for i in range(len(row) - 1, 0, -1): # 0 is excluded
            if row[i] == row[i - 1] and row[i] != 0:
                row[i] = row[i] * 2
                row[i - 1] = 0

            slideRight(board)
    


def slideRight(board):
    new_board = tempGrid()
    for row in range(len(board)):
        j = len(new_board[0]) - 1

        for col in range(len(board[row]) - 1, -1, -1):
            if board[row][col] != 0:
                new_board[row][j] = board[row][col]
                j -= 1

    return new_board


def slideLeft(board):
    new_board = tempGrid()
    for row in range(len(board)):
        j = 0

        for col in range(len(board[row]) - 1, -1, -1):
            if board[row][col] != 0:
                new_board[row][j] = board[row][col]
                j += 1

    board = new_board

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
# shiftRight(board)
shiftRight(board)
# shiftUp(board)
# slideRight(board)
print_board_numbers(board)


