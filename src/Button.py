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
        pass

    def hover(self):
        pass