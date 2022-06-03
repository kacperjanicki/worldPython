
import random
from world.organisms.animals.Animal import Animal


class Antelope(Animal):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Antelope"
        self.skin = "A"
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 4
        self.baseStrength = 4
        self.initiative = 4
        self.id = 5

    def move(self):
        if(random.random() < 0.5):
            range = 1
        else:
            range = 2

        if(random.random() < 0.5):
            if(random.random() < 0.5):
                if(self.x < self.world.size - range):
                    self.x += range
                else:
                    self.x -= range
            else:
                if(self.y < self.world.size - range):
                    self.y += range
                else:
                    self.y -= range
        else:
            if(random.random() < 0.5):
                if(self.x > 0):
                    self.x -= range
                else:
                    self.x += range
            else:
                if(self.y > 0):
                    self.y -= range
                else:
                    self.y += range

    def action(self):
        if(self.alive):
            self.move()

    def collision(self, organism):
        if(self.id == organism.getId()):
            self.spawnNewOrgnism(self, organism, self.world)
            return

        if(random, random() < 0.5):
            self.kill()
            self.world.events.append("{} died to {}".format(self.name, organism.getName()))
            return

        freeSpaces = []
        if(random.random() < 0.5):
            range = 1
        else:
            range = 2

        for x in range(self.x - range, self.x + range):
            for y in range(self.y - range, self.y + range):
                if(x >= 0 and x < self.world.size and y >= 0 and y < self.world.size):
                    if(x >= 0 and x < self.world.size and y >= 0 and y < self.world.size):
                        if(x != y and (x == self.x or y == self.y)):
                            if(self.world.isFreeFromStronger(x, y, self.strength)):
                                freeSpaces.append([x, y])

        if(len(freeSpaces) > 0):
            randomIndex = random.randint(0, freeSpaces.__len__() - 1)
            self.prevX = self.x
            self.prevY = self.y
            self.x = freeSpaces[randomIndex][0]
            self.y = freeSpaces[randomIndex][1]
            self.world.events.append("{} escaped from {}".format(self.name, organism.getName()))
        else:
            self.kill()
            self.world.events.append("{} died to {}".format(self.name, organism.getName()))
