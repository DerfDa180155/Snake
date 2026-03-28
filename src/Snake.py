import random

class Snake:
    def __init__(self):
        self.map = []

        self.sizeX = 20
        self.sizeY = 20

        self.generateEmptyBoard()

    def generateEmptyBoard(self):
        self.map = []
        for i in range(self.sizeY):
            temp = []
            for j in range(self.sizeX):
                temp.append("")
            self.map.append(temp)

    def movePlayer(self):
        pass

    def spawnFood(self):
        x = random.randint(0, self.sizeX-1)
        y = random.randint(0, self.sizeY-1)

        while not self.isEmpty(x, y):
            x = random.randint(0, self.sizeX - 1)
            y = random.randint(0, self.sizeY - 1)

        self.map[y][x] = "x"

    def isEmpty(self, x, y):
        return self.map[y][x] == ""