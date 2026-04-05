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

        self.playerDirection = 0

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
        x = self.player[len(self.player)-1][1]
        y = self.player[len(self.player)-1][0]
        moved = False

        match (self.playerDirection):
            case 0:
                if x+1 < self.sizeX:
                    self.player.append([y, x+1])
                    self.map[y][x+1] = self.playerField
                    moved = True
            case 1:
                if y+1 < self.sizeY:
                    self.player.append([y+1, x])
                    self.map[y+1][x] = self.playerField
                    moved = True
            case 2:
                if x-1 >= 0:
                    self.player.append([y, x-1])
                    self.map[y][x-1] = self.playerField
                    moved = True
            case 3:
                if y-1 >= 0:
                    self.player.append([y-1, x])
                    self.map[y-1][x] = self.playerField
                    moved = True

        if moved:
            self.map[self.player[0][0]][self.player[0][1]] = self.emptyField
            self.player.pop(0)

    def growPlayer(self):
        self.spawnFood()

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