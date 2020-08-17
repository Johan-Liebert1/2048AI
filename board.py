import pygame, random

from colors import colors
from tile import Tile

WIN_WIDTH = WIN_HEIGHT = 600

class Board:
    def __init__(self, window, dimension):
        self.dimension = dimension
        self.window = window
        self.board = [[0] * dimension for _ in range(dimension)]

    def get_random_nums(self):
        return random.randrange(self.dimension), random.randrange(self.dimension)

    def find_random_empty_space(self):
        row, col = self.get_random_nums()

        while self.board[row][col] != 0:
            row, col = self.get_random_nums()

        return row, col


    def get_board_ready(self):
        row, col = self.find_random_empty_space()

        # 70% of the time random number is 2, rest of the time it's 4

        rand_num = random.randrange(1, 101)

        number = 2 if rand_num < 70 else 4

        self.board[row][col] = number

        tile = Tile(WIN_WIDTH // 6, number, row, col)
        tile.draw(self.window)


    def move_tiles(self, direction):
        # direction can be UP, DOWN, LEFT, RIGHT
        direction = direction.lower()


    def draw(self, window):
        window.fill(colors['BOARD_COLOR'])
        pygame.display.flip()

    