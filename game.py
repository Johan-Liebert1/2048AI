import pygame, random

from colors import colors
from board import Board

WIN_WIDTH = WIN_HEIGHT = 600

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

def draw_game_window():
    board = Board(window, 6)
    board.draw(window)

    board.get_board_ready()

    pygame.display.update()


# MAIN LOOP
draw_game_window()
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

    
