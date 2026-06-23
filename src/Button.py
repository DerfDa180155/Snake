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
        self.isleftClicked = False
        self.isrightClicked = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))

        textSize = 50
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)

        text = font.render(self.onClick, True, (0, 150, 120))
        newRect = text.get_rect()
        newRect.centerx = self.x + self.sizeX/2
        newRect.centery = self.y + self.sizeY/2
        self.screen.blit(text, newRect)

    def clicked(self, mx, my, mouseClick):
        if self.hover(mx, my) and mouseClick[0]:
            self.isleftClicked = True
        elif self.hover(mx, my) and mouseClick[2]:
            self.isrightClicked = True
        else:
            self.isleftClicked = False
            self.isrightClicked = False
        return self.isleftClicked

    def hover(self, mx, my):
        temp = pygame.Rect(self.x, self.y, self.sizeX, self.sizeY)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered
