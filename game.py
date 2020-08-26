import pygame, random

from colors import colors
from board import Board

WIN_WIDTH = WIN_HEIGHT = 600

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
board = None

# MAIN LOOP
board = Board(window, 6)
board.draw()

pygame.display.update()
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(30)
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        board.move_tiles('up')
        pygame.time.wait(300) # time in ms

    elif keys[pygame.K_DOWN]:
        board.move_tiles('down')
        pygame.time.wait(300) # time in ms

    elif keys[pygame.K_RIGHT]:
        board.move_tiles('right')
        pygame.time.wait(300) # time in ms

    elif keys[pygame.K_LEFT]:
        board.move_tiles('left')
        pygame.time.wait(300) # time in ms

    elif keys[pygame.K_SPACE]:
        board.go_back()

    

    
