import pygame

from colors import colors

WIN_WIDTH = WIN_HEIGHT = 600

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))



class Tile:
    FONT = pygame.font.SysFont("Arial", 36)

    def __init__(self, dimension, number, row, col):
        self.height = dimension
        self.width = dimension
        self.number = number
        self.color = colors[str(number)]
        self.position = {
            'x' : row * self.width,
            'y' : col * self.height
        }

    def draw(self, window):

        pygame.draw.rect(
            window, 
            self.color, 
            (
                self.position['x'],
                self.position['y'],
                self.width,
                self.height
            )
        )

        if self.number <= 16:
            text_color = colors['BLACK']
        
        else:
            text_color = colors['BOARD_COLOR']

        text = self.FONT.render(str(self.number), True, text_color)
        text_height = text.get_height()
        text_width = text.get_width()

        window.blit(
            text, 
            (
                self.position['x'] + (self.width - text_width) // 2, 
                self.position['y'] + (self.height - text_height) // 2
            )
        )


class Board:
    def __init__(self, dimension):
        self.dimension = dimension
        self.board = [[0] * dimension for _ in range(dimension)]

    def draw(self, window):
        window.fill(colors['BOARD_COLOR'])
        pygame.display.flip()

    


def draw_game_window():
    board = Board(6)
    board.draw(window)

    tile = Tile(WIN_WIDTH // 6, 8, 2, 2)
    tile.draw(window)

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

    

    
