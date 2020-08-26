import pygame

from colors import colors

pygame.font.init()

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

        if self.number <= 16 or self.number == 128 or self.number == 256:
            text_color = colors['BLACK']
        
        else:
            text_color = colors['WHITE']

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
