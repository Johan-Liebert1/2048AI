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
        self.board = np.array([[0] * dimension for _ in range(dimension)])
        self.put_random_tile()
        self.put_random_tile()

    def giveTempBoard(self):
        return np.array([[0] * self.dimension for _ in range(self.dimension)])
        

    def makeBoardGrid(self):
        for i in range(self.dimension):
            pygame.draw.line(
                    self.window, 
                    colors['BOARD_BORDER'],
                    ( 0, i * (WIN_WIDTH // self.dimension) ), ( WIN_WIDTH, i * (WIN_WIDTH // self.dimension) ),
                    4 # line width
                )

            for j in range(self.dimension):

                pygame.draw.line(
                    self.window,
                    colors['BOARD_BORDER'],
                    ( j * (WIN_WIDTH // self.dimension), 0 ), ( j * (WIN_WIDTH // self.dimension), WIN_WIDTH ),
                    4 # line width
                )

            pygame.display.update()

    def get_random_nums(self):
        return random.randrange(self.dimension), random.randrange(self.dimension)


    def find_random_empty_space(self):
        row, col = self.get_random_nums()

        while self.board[row][col] != 0:
            row, col = self.get_random_nums()

        return row, col


    def put_random_tile(self):
        row, col = self.find_random_empty_space()

        # 90% of the time random number is 2, rest of the time it's 4 

        number = 2 if random.randrange(1, 101) <= 90 else 4

        self.board[row][col] = number


    def place_tiles(self):

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
        if direction == 'up':
            self.shiftUp()

        elif direction == 'down':
            self.shiftDown()

        elif direction == 'right':
            self.shiftRight()

        elif direction == 'left':
            self.shiftLeft()

        self.put_random_tile()

        self.draw()


    def shiftRight(self):
        self.slideRight()
        for row in range(len(self.board)):
            for i in range(len(self.board[row]) - 1, 0, -1): # 0 is excluded
                if self.board[row][i] == self.board[row][i - 1]:
                    self.board[row][i] = self.board[row][i] * 2
                    self.board[row][i-1] = 0
            self.slideRight()


    def slideRight(self):
        tempBoard = self.giveTempBoard()

        for row in range(len(self.board)):
            j = len(tempBoard) - 1
            for col in range(len(self.board) - 1, -1, -1):
        
                if self.board[row][col] != 0:
                    tempBoard[row][j] = self.board[row][col]
                    j -= 1

        self.board = tempBoard

    def shiftLeft(self):
        self.slideLeft()
        for row in range(len(self.board)):
            for i in range(0, len(self.board) - 1): # 0 is excluded
                if self.board[row][i] == self.board[row][i + 1]:
                    self.board[row][i] = self.board[row][i] * 2
                    self.board[row][i + 1] = 0
            self.slideLeft()

    def slideLeft(self):
        tempBoard = self.giveTempBoard()

        for row in range(len(self.board)):
            j = 0
            for col in range(len(self.board)):
                
                if self.board[row][col] != 0:
                    tempBoard[row][j] = self.board[row][col]
                    j += 1
        self.board = tempBoard


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


    def isGameOver(self):
        for i in range(self.dimension):
            for j in range(self.dimension):

                if self.board[i][j] == 0:
                    return False
                
                if i != 3 and self.board[i][j] == self.board[i + 1][j]:
                    return False
                
                if j != 3 and self.board[i][j] == self.board[i][j + 1]:
                    return False    
            
        return True
        

    def draw(self):
        self.window.fill(colors['BOARD_COLOR'])
        pygame.display.flip()
        self.place_tiles()
        self.makeBoardGrid()
