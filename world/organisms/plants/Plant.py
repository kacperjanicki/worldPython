
import random
from world.organisms.Organism import Organism


class Plant(Organism):
    def __init__(self, world):
        super().__init__(world)
        self.alive = True
        self.strength = 0
        self.baseStrength = 0
        self.initiative = 0
        self.skin = None
        self.name = None
        self.directionX = None
        self.directionY = None
        self.animal = False
        self.sewRange = 1

    def sew(self):
        freeSpaces = []

        for x in range(self.x - self.sewRange, self.x + self.sewRange):
            for y in range(self.y - self.sewRange, self.y + self.sewRange):
                if(x >= 0 and x < self.world.size and y >= 0 and y < self.world.size):
                    if(x >= 0 and x < self.world.size and y >= 0 and y < self.world.size):
                        if(self.world.isFree(x, y)):
                            freeSpaces.append([x, y])

        if(len(freeSpaces) > 0):
            randomIndex = random.randint(0, freeSpaces.__len__() - 1)
            self.prevX = self.x
            self.prevY = self.y
            self.x = freeSpaces[randomIndex][0]
            self.y = freeSpaces[randomIndex][1]

    def action(self):
        self.sew()
