

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
        pass
