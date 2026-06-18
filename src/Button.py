import pygame

class Button:
    def __init__(self, screen, x, y, sizeX, sizeY, color, onCLick):
        self.screen = screen
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color
        self.onClick = onCLick
        self.isHovered = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))

    def hover(self, mx, my):
        temp = pygame.Rect(self.x, self.y, self.sizeX, self.sizeY)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered
