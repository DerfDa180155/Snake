import pygame

import Snake

class main:
    def __init__(self):
        pygame.init()
        pygame.display.init()

        pygame.display.gl_set_attribute(pygame.GL_ACCELERATED_VISUAL, 0)
        pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)

        self.windowWidth = 1500
        self.windowHeight = 1500

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.GL_DOUBLEBUFFER | pygame.RESIZABLE)
        pygame.display.set_caption("Snake by David Derflinger")

        self.clock = pygame.time.Clock()
        self.running = True

        self.snake = Snake.Snake()

        self.run()

    def run(self):
        delay = 0
        directionChanged = False
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Quit the Game
                        self.running = False
                    elif (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake.playerDirection != 1 and not self.snake.gameOver and not self.snake.paused and not directionChanged:
                        directionChanged = True
                        self.snake.playerDirection = 3
                    elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.snake.playerDirection != 0 and not self.snake.gameOver and not self.snake.paused and not directionChanged:
                        directionChanged = True
                        self.snake.playerDirection = 2
                    elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake.playerDirection != 3 and not self.snake.gameOver and not self.snake.paused and not directionChanged:
                        directionChanged = True
                        self.snake.playerDirection = 1
                    elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.snake.playerDirection != 2 and not self.snake.gameOver and not self.snake.paused and not directionChanged:
                        directionChanged = True
                        self.snake.playerDirection = 0
                    elif event.key == pygame.K_x and self.snake.gameOver:
                        self.snake.reset()
                    elif event.key == pygame.K_f:
                        self.snake.paused = not self.snake.paused

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

            self.drawBoardWithWindowSize(self.windowWidth, self.windowHeight)

            if delay <= 0:
                directionChanged = False
                self.snake.movePlayer()
                #self.snake.spawnFood()
                delay = 10

            delay -= 1

            if self.snake.paused:
                smaller = self.windowWidth
                if self.windowHeight < self.windowWidth:
                    smaller = self.windowHeight
                self.drawPaused(self.windowWidth/2-(smaller/1.5)/2, self.windowHeight/2-(smaller/2)/2, smaller/1.5, smaller/2, int(smaller/30))

            if self.snake.gameOver:
                smaller = self.windowWidth
                if self.windowHeight < self.windowWidth:
                    smaller = self.windowHeight
                self.drawGameOver(self.windowWidth/2-(smaller/1.5)/2, self.windowHeight/2-(smaller/2)/2, smaller/1.5, smaller/2, int(smaller/30))

            pygame.display.flip()
            self.clock.tick(60)

    def drawBoardWithWindowSize(self, windowWidth, windowHeight):
        smaller = windowWidth
        if windowHeight < windowWidth:
            smaller = windowHeight
        self.drawBoard(windowWidth/2-smaller/2.5, windowHeight/2-smaller/2.5, smaller/1.25, smaller/1.25, 10)

    def drawBoard(self, startX, startY, width, height, gapSize):
        for y in range(self.snake.sizeY):
            for x in range(self.snake.sizeX):
                color = (255, 255, 255)
                if self.snake.map[y][x] == self.snake.emptyField:
                    color = (255, 255, 255)
                elif self.snake.map[y][x] == self.snake.foodField:
                    color = (255, 0, 0)
                elif self.snake.map[y][x] == self.snake.playerField:
                    color = (0, 255, 64)
                pygame.draw.rect(self.screen, color, (startX + width/self.snake.sizeX*x, startY + height/self.snake.sizeY*y, (width/self.snake.sizeX)-gapSize, (height/self.snake.sizeY)-gapSize))

    def drawPaused(self, posX, posY, sizeX, sizeY, textSize):
        pygame.draw.rect(self.screen, (10, 10, 10), (posX, posY, sizeX, sizeY))

        baseSize = 50 + textSize

        text = "Paused"
        textSize = baseSize + 50
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)
        text = font.render(text, True, (255, 255, 255))
        newRect = text.get_rect()
        newRect.centerx = posX + sizeX / 2
        newRect.centery = posY + sizeY / 4
        self.screen.blit(text, newRect)

        text = "press f to resume"
        textSize = baseSize - 20
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)
        text = font.render(text, True, (255, 255, 255))
        newRect = text.get_rect()
        newRect.centerx = posX + sizeX / 2
        newRect.centery = posY + sizeY / 2
        self.screen.blit(text, newRect)

    def drawGameOver(self, posX, posY, sizeX, sizeY, textSize):
        pygame.draw.rect(self.screen, (10, 10, 10), (posX, posY, sizeX, sizeY))

        baseSize = 50 + textSize

        text = "GameOver"
        textSize = baseSize+50
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)
        text = font.render(text, True, (255, 255, 255))
        newRect = text.get_rect()
        newRect.centerx = posX + sizeX/2
        newRect.centery = posY + sizeY/4
        self.screen.blit(text, newRect)

        text = "Score: " + str(self.snake.score)
        textSize = baseSize-20
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)
        text = font.render(text, True, (255, 255, 255))
        newRect = text.get_rect()
        newRect.centerx = posX + sizeX / 2
        newRect.centery = posY + sizeY / 2
        self.screen.blit(text, newRect)

        text = "press x to restart"
        textSize = baseSize-30
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)
        text = font.render(text, True, (255, 255, 255))
        newRect = text.get_rect()
        newRect.centerx = posX + sizeX / 2
        newRect.centery = posY + sizeY / 1.5
        self.screen.blit(text, newRect)


if __name__ == "__main__":
    main()
