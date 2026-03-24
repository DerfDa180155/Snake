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

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.GL_DOUBLEBUFFER)
        pygame.display.set_caption("Snake by David Derflinger")

        self.clock = pygame.time.Clock()
        self.running = True

        self.snake = Snake.Snake()

        self.run()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Quit the Game
                        self.running = False

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

            self.drawBoard(100, 100)



            pygame.display.flip()
            self.clock.tick(60)

    def drawBoard(self, startX, startY):
        for y in range(self.snake.sizeY):
            for x in range(self.snake.sizeX):
                color = (255, 0, 0)
                if self.snake.map[y][x] == "":
                    color = (255, 255, 255)
                pygame.draw.rect(self.screen, color, (startX + 30*x, startY + 30*y, 25, 25))


if __name__ == "__main__":
    main()
