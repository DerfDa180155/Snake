import pygame

class Button:
    def __init__(self, screen, x, y, sizeX, sizeY, onCLick):
        self.screen = screen
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.onClick = onCLick

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, self.sizeX, self.sizeY))

    def hover(self):
        pass