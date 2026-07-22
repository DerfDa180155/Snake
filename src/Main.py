import pygame

import Snake
import Button

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
        self.speedup = 10

        self.menu = "main"

        self.mainButtons = [Button.Button(self.screen, 400, 300, 700, 200, (255, 255, 255), "Start"),
                            Button.Button(self.screen, 400, 600, 700, 200, (255, 255, 255), "Settings"),
                            Button.Button(self.screen, 400, 900, 700, 200, (255, 255, 255), "Quit")]
        self.gameButtons = [Button.Button(self.screen, 50, 50, 150, 60, (255, 255, 255), "Back")]
        self.settingsButtons = [Button.Button(self.screen, 50, 50, 150, 60, (255, 255, 255), "Back"),
                                Button.Button(self.screen, 100, 300, 100, 50, (255, 255, 255), "X+"),
                                Button.Button(self.screen, 250, 300, 100, 50, (255, 255, 255), "X-"),
                                Button.Button(self.screen, 100, 400, 100, 50, (255, 255, 255), "Y+"),
                                Button.Button(self.screen, 250, 400, 100, 50, (255, 255, 255), "Y-"),
                                Button.Button(self.screen, 100, 500, 250, 50, (255, 255, 255), "speedup+"),
                                Button.Button(self.screen, 100, 600, 250, 50, (255, 255, 255), "speedup-"),
                                Button.Button(self.screen, 100, 700, 250, 50, (255, 255, 255), "food+"),
                                Button.Button(self.screen, 100, 800, 250, 50, (255, 255, 255), "food-")]

        self.run()

    def run(self):
        delay = 0
        directionChanged = False
        oldMousePressed = pygame.mouse.get_pressed()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Quit the Game
                        if self.menu == "main":
                            self.running = False
                        elif self.menu == "game" or self.menu == "settings":
                            self.menu = "main"
                    if self.menu == "main":
                        if event.key == pygame.K_SPACE:
                            self.snake.reset()
                            self.menu = "game"
                    elif self.menu == "game":
                        if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake.playerDirection != 1 and not self.snake.gameOver and not self.snake.isStartScreen and not self.snake.paused and not directionChanged:
                            directionChanged = True
                            self.snake.playerDirection = 3
                        elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.snake.playerDirection != 0 and not self.snake.gameOver and not self.snake.isStartScreen and not self.snake.paused and not directionChanged:
                            directionChanged = True
                            self.snake.playerDirection = 2
                        elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake.playerDirection != 3 and not self.snake.gameOver and not self.snake.isStartScreen and not self.snake.paused and not directionChanged:
                            directionChanged = True
                            self.snake.playerDirection = 1
                        elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.snake.playerDirection != 2 and not self.snake.gameOver and not self.snake.isStartScreen and not self.snake.paused and not directionChanged:
                            directionChanged = True
                            self.snake.playerDirection = 0
                        elif event.key == pygame.K_x and self.snake.gameOver:
                            self.snake.reset()
                        elif event.key == pygame.K_f:
                            self.snake.paused = not self.snake.paused

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

            mx, my = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            mousePressedUp = []
            mousePressedDown = []
            for i in range(len(mousePressed)):
                mousePressedUp.append(not mousePressed[i] and oldMousePressed[i])
                mousePressedDown.append(mousePressed[i] and not oldMousePressed[i])

            oldMousePressed = mousePressed

            match self.menu:
                case "main":
                    textSize = 50
                    font = pygame.font.Font(pygame.font.get_default_font(), textSize)

                    text = font.render("Snake", True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.y = textSize
                    self.screen.blit(text, newRect)

                    for button in self.mainButtons:
                        button.draw()
                        button.clicked(mx=mx, my=my, mouseClick=mousePressedUp)
                        if button.isleftClicked:
                            match button.onClick:
                                case "Start":
                                    self.snake.reset()
                                    self.menu = "game"
                                case "Settings":
                                    self.menu = "settings"
                                case "Quit":
                                    self.running = False

                case "game":
                    self.drawBoardWithWindowSize(self.windowWidth, self.windowHeight)

                    textSize = 50
                    font = pygame.font.Font(pygame.font.get_default_font(), textSize)

                    text = font.render("Score: " + str(self.snake.score), True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.y = textSize
                    self.screen.blit(text, newRect)

                    if self.snake.isStartScreen and self.snake.startScreenCounter >= 0:
                        text = font.render("Start: " + str(int(self.snake.startScreenCounter/6)+1), True, (255, 255, 255))
                        newRect = text.get_rect()
                        newRect.centerx = self.windowWidth / 2
                        newRect.y = 1400
                        self.screen.blit(text, newRect)

                    if delay <= 0:
                        directionChanged = False
                        self.snake.update()
                        #self.snake.spawnFood()
                        delay = 10

                        delay -= int(self.snake.score/self.speedup)

                    delay -= 1

                    if self.snake.paused:
                        smaller = self.windowWidth
                        if self.windowHeight < self.windowWidth:
                            smaller = self.windowHeight
                        self.drawPaused(self.windowWidth/2-(smaller/1.5)/2, self.windowHeight/2-(smaller/2)/2, smaller/1.5, smaller/2, int(smaller/50))

                    if self.snake.gameOver:
                        smaller = self.windowWidth
                        if self.windowHeight < self.windowWidth:
                            smaller = self.windowHeight
                        self.drawGameOver(self.windowWidth/2-(smaller/1.5)/2, self.windowHeight/2-(smaller/2)/2, smaller/1.5, smaller/2, int(smaller/50))

                    for button in self.gameButtons:
                        button.draw(30)
                        button.clicked(mx=mx, my=my, mouseClick=mousePressedUp)
                        if button.isleftClicked:
                            match button.onClick:
                                case "Back":
                                    self.menu = "main"

                case "settings":
                    textSize = 50
                    font = pygame.font.Font(pygame.font.get_default_font(), textSize)

                    text = font.render("Settings", True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.centerx = self.windowWidth / 2
                    newRect.y = textSize
                    self.screen.blit(text, newRect)

                    textSize = 35
                    font = pygame.font.Font(pygame.font.get_default_font(), textSize)

                    text = font.render("x: " + str(self.snake.sizeX), True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.x = 400
                    newRect.y = 307
                    self.screen.blit(text, newRect)

                    text = font.render("y: " + str(self.snake.sizeY), True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.x = 400
                    newRect.y = 407
                    self.screen.blit(text, newRect)

                    text = font.render("Speedup: " + str(self.speedup), True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.x = 400
                    newRect.y = 507
                    self.screen.blit(text, newRect)

                    text = font.render("Food: " + str(1), True, (255, 255, 255))
                    newRect = text.get_rect()
                    newRect.x = 400
                    newRect.y = 707
                    self.screen.blit(text, newRect)

                    for button in self.settingsButtons:
                        button.draw(30)
                        button.clicked(mx=mx, my=my, mouseClick=mousePressedUp)
                        if button.isleftClicked:
                            match button.onClick:
                                case "Back":
                                    self.menu = "main"
                                case "X+":
                                    self.snake.sizeX += 1
                                    if self.snake.sizeX > 40:
                                        self.snake.sizeX = 40
                                case "X-":
                                    self.snake.sizeX -= 1
                                    if self.snake.sizeX < 2:
                                        self.snake.sizeX = 2
                                case "Y+":
                                    self.snake.sizeY += 1
                                    if self.snake.sizeY > 40:
                                        self.snake.sizeY = 40
                                case "Y-":
                                    self.snake.sizeY -= 1
                                    if self.snake.sizeY < 2:
                                        self.snake.sizeY = 2
                                case "speedup+":
                                    self.speedup += 1
                                    if self.speedup > 20:
                                        self.speedup = 20
                                case "speedup-":
                                    self.speedup -= 1
                                    if self.speedup < 1:
                                        self.speedup = 1
                                case "food+":
                                    print("food +")
                                case "food-":
                                    print("food -")


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

        text = "Score: " + str(self.snake.score+1)
        textSize = baseSize - 30
        font = pygame.font.Font(pygame.font.get_default_font(), textSize)
        text = font.render(text, True, (255, 255, 255))
        newRect = text.get_rect()
        newRect.centerx = posX + sizeX / 2
        newRect.centery = posY + sizeY / 1.5
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
