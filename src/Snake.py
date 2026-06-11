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

        self.gameOver = False
        self.score = -1

        self.isStartScreen = True
        self.startScreenCounter = 18
        self.paused = False

        self.generateEmptyBoard()

        self.spawnFood()
        self.spawnPlayer()

    def reset(self):
        self.map = []
        self.player = []

        self.playerDirection = 0

        self.lastFoodLocation = [-1, -1]

        self.isStartScreen = True
        self.startScreenCounter = 18
        self.paused = False
        self.gameOver = False
        self.score = 0

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
        self.player.append([int(self.sizeY / 2), int(self.sizeX / 2) - 2])
        self.map[self.player[0][0]][self.player[0][1]] = self.playerField

        self.player.append([int(self.sizeY / 2), int(self.sizeX / 2) - 1])
        self.map[self.player[1][0]][self.player[1][1]] = self.playerField

        self.player.append([int(self.sizeY / 2), int(self.sizeX / 2)])
        self.map[self.player[2][0]][self.player[2][1]] = self.playerField

        print(self.player)

    def update(self):
        if self.isStartScreen:
            print(self.startScreenCounter)
            self.startScreenCounter -= 1
            if self.startScreenCounter == 0:
                self.isStartScreen = False
        elif not self.paused and not self.gameOver:
            self.movePlayer()

    def movePlayer(self):
        x = self.player[len(self.player)-1][1]
        y = self.player[len(self.player)-1][0]
        moved = False

        match (self.playerDirection):
            case 0:
                if x+1 < self.sizeX:
                    if self.map[y][x+1] != self.playerField:
                        self.player.append([y, x+1])
                        self.map[y][x+1] = self.playerField
                        moved = True
            case 1:
                if y+1 < self.sizeY:
                    if self.map[y+1][x] != self.playerField:
                        self.player.append([y+1, x])
                        self.map[y+1][x] = self.playerField
                        moved = True
            case 2:
                if x-1 >= 0:
                    if self.map[y][x-1] != self.playerField:
                        self.player.append([y, x-1])
                        self.map[y][x-1] = self.playerField
                        moved = True
            case 3:
                if y-1 >= 0:
                    if self.map[y-1][x] != self.playerField:
                        self.player.append([y-1, x])
                        self.map[y-1][x] = self.playerField
                        moved = True

        if not moved:
            self.gameOver = True

        if moved and not self.growPlayer():
            self.map[self.player[0][0]][self.player[0][1]] = self.emptyField
            self.player.pop(0)
        elif not self.gameOver:
            self.score += 1

    def growPlayer(self):
        foodLocation = self.lastFoodLocation
        playerX = self.player[len(self.player)-1][1]
        playerY = self.player[len(self.player)-1][0]
        self.spawnFood()
        return playerY == foodLocation[0] and playerX == foodLocation[1]

    def foodPlaced(self):
        return self.map[self.lastFoodLocation[0]][self.lastFoodLocation[1]] == self.foodField

    def spawnFood(self):
        if self.foodPlaced():
            return

        x = random.randint(0, self.sizeX-1)
        y = random.randint(0, self.sizeY-1)

        while not self.isEmpty(x, y):
            x = random.randint(0, self.sizeX - 1)
            y = random.randint(0, self.sizeY - 1)

        self.map[y][x] = self.foodField
        self.lastFoodLocation = [y, x]

    def isEmpty(self, x, y):
        return self.map[y][x] == self.emptyField