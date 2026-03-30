import random

class Snake:
    def __init__(self):
        self.map = []

        self.sizeX = 20
        self.sizeY = 20

        self.player = []

        self.emptyField = ""
        self.foodField = "x"
        self.playerField = "o"

        self.lastFoodLocation = [-1, -1]

        self.generateEmptyBoard()

        self.spawnFood()
        self.spawnPlayer()

    def generateEmptyBoard(self):
        self.map = []
        for i in range(self.sizeY):
            temp = []
            for j in range(self.sizeX):
                temp.append(self.emptyField)
            self.map.append(temp)

    def spawnPlayer(self):
        self.player.append([int(self.sizeX/2), int(self.sizeY/2)])
        self.map[self.player[0][1]][self.player[0][0]] = self.playerField

    def movePlayer(self):
        pass

    def foodPlaced(self):
        return self.map[self.lastFoodLocation[1]][self.lastFoodLocation[0]] == self.foodField

    def spawnFood(self):
        if self.foodPlaced():
            return

        x = random.randint(0, self.sizeX-1)
        y = random.randint(0, self.sizeY-1)

        while not self.isEmpty(x, y):
            x = random.randint(0, self.sizeX - 1)
            y = random.randint(0, self.sizeY - 1)

        self.map[y][x] = self.foodField
        self.lastFoodLocation = [x, y]

    def isEmpty(self, x, y):
        return self.map[y][x] == self.emptyField