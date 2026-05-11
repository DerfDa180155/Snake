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
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Quit the Game
                        self.running = False
                    elif (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake.playerDirection != 1:
                        self.snake.playerDirection = 3
                    elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.snake.playerDirection != 0:
                        self.snake.playerDirection = 2
                    elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake.playerDirection != 3:
                        self.snake.playerDirection = 1
                    elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.snake.playerDirection != 2:
                        self.snake.playerDirection = 0
                    elif event.key == pygame.K_x and self.snake.gameOver:
                        self.snake.reset()

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

            self.drawBoardWithWindowSize(self.windowWidth, self.windowHeight)

            if delay <= 0:
                self.snake.movePlayer()
                #self.snake.spawnFood()
                delay = 10

            delay -= 1

            if self.snake.gameOver:
                self.drawGameOver(self.windowWidth/2-500, self.windowHeight/2-400, 1000, 800)

            pygame.display.flip()
            self.clock.tick(60)

    def drawBoardWithWindowSize(self, windowWidth, windowHeight):
        self.drawBoard(windowWidth/2-windowWidth/3, windowHeight/2-windowHeight/3, windowWidth/1.5, windowHeight/1.5, 10)

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

    def drawGameOver(self, posX, posY, sizeX, sizeY):
        pygame.draw.rect(self.screen, (10, 10, 10), (posX, posY, sizeX, sizeY))

        text = "GameOver"
        textSize = 100
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)
        text = font.render(text, True, (255, 255, 255))
        newRect = text.get_rect()
        newRect.centerx = posX + sizeX/2
        newRect.centery = posY + sizeY/4
        self.screen.blit(text, newRect)

        text = "Score: " + str(self.snake.score)
        textSize = 30
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)
        text = font.render(text, True, (255, 255, 255))
        newRect = text.get_rect()
        newRect.centerx = posX + sizeX / 2
        newRect.centery = posY + sizeY / 2
        self.screen.blit(text, newRect)

        text = "press x to restart"
        textSize = 20
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)
        text = font.render(text, True, (255, 255, 255))
        newRect = text.get_rect()
        newRect.centerx = posX + sizeX / 2
        newRect.centery = posY + sizeY / 1.5
        self.screen.blit(text, newRect)


if __name__ == "__main__":
    main()
