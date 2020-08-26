import pygame, random
import numpy as np
from termcolor import colored

from colors import colors
from tile import Tile

WIN_WIDTH = WIN_HEIGHT = 600

class Board:
    def __init__(self, window, dimension):
        self.dimension = dimension
        self.window = window
        # self.board = np.array([[0] * dimension for _ in range(dimension)])

        self.board = np.array([
            [4,0,8,8,0,4],
            [0,0,0,0,0,0],
            [16,0,0,0,0,16],
            [16,0,0,0,0,16],
            [0,0,0,0,0,0],
            [2,0,8,8,0,2],
        ])

    def get_random_nums(self):
        return random.randrange(self.dimension), random.randrange(self.dimension)


    # def find_random_empty_space(self):
    #     row, col = self.get_random_nums()

    #     while self.board[row][col] != 0:
    #         row, col = self.get_random_nums()

    #     return row, col


    # def put_random_tile(self):
    #     row, col = self.find_random_empty_space()

    #     # 90% of the time random number is 2, rest of the time it's 4 

    #     number = 2 if random.randrange(1, 101) <= 90 else 4

    #     self.board[row][col] = number
    #     self.place_tiles()


    def place_tiles(self):
        self.window.fill(colors['BOARD_COLOR'])
        pygame.display.flip()

        for i in range(self.dimension):
            for j in range(self.dimension):

                if self.board[i][j] != 0:

                    tile = Tile(
                        WIN_WIDTH // self.dimension,
                        self.board[i][j],
                        j,i 
                    )

                    tile.draw(self.window)

            pygame.display.update()
        

    def move_tiles(self, direction):
        # direction can be UP, DOWN, LEFT, RIGHT
        direction = direction.lower()

        if direction == 'up':
            self.shiftUp()

        elif direction == 'down':
            self.shiftDown()

        elif direction == 'right':
            self.shiftRight()

        elif direction == 'left':
            self.shiftLeft()

        self.draw()

        self.print_board_numbers(self.board)

    def shiftRight(self):
    # newBoard = newGrid()
        for row in self.board:
            for i in range(len(row) - 1, 0, -1): # 0 is excluded
                if row[i] == row[i - 1]:
                    row[i] = row[i] * 2
                    row[i-1] = 0
            self.slideRight()


    def slideRight(self):
        for row in self.board:
            for i in range(len(self.board) - 1):
                if row[i] != 0 and row[i + 1] == 0:
                    row[i + 1] = row[i]
                    row[i] = 0


    def slideLeft(self):
        for row in self.board:
            for i in range(len(self.board) - 1):
                if row[i + 1] != 0 and row[i] == 0:
                    row[i] = row[i + 1]
                    row[i + 1] = 0


    def shiftLeft(self):
        self.shiftRight()

        for _ in range(len(self.board)):
            self.slideLeft()


    def shiftDown(self):
        self.board = self.board.T

        self.shiftRight()
        self.board = self.board.T


    def shiftUp(self):
        self.board = self.board.T

        self.shiftLeft()
        self.board = self.board.T

    
    def print_board_numbers(self, board):
        string = ''
        for i in range(len(board)):
            string += '\n\n'
            for j in range(len(board)):
                color = 'green' if board[i][j] != 0 else 'white'

                string += colored(board[i][j], color) + "    "
        print(string, "\n\n")


    def draw(self):

        self.place_tiles()

    