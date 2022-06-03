
import random


class Organism():
    def __init__(self, world):
        self.id = None
        self.x = None
        self.y = None
        self.prevX = None
        self.prevY = None
        self.strength = 0
        self.baseStrength = 0
        self.initiative = 0
        self.world = world
        self.animal = False
        self.alive = True
        self.skin = None
        self.name = None
        self.directionX = None
        self.directionY = None

    def getId(self):
        return self.id

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getStrength(self):
        return self.strength

    def setStrength(self, strength):
        self.strength = strength

    def getName(self):
        return self.name

    def isAnimal(self):
        return self.animal

    def isAlive(self):
        return self.alive

    def kill(self):
        self.alive = False

    def notMoved(self):
        self.prevX = self.x
        self.prevY = self.y

    def moveBack(self):
        self.x = self.prevX
        self.y = self.prevY

    def action(self):
        pass

    def spawnNewOrgnism(self, organism):
        smallerX = None
        biggerX = None
        smallerY = None
        biggerY = None

        if(self.x > organism.getx()):
            smallerX = organism.getx()
            biggerX = self.x
        else:
            smallerX = self.x
            biggerX = organism.getx()

        if(self.y > organism.gety()):
            smallerY = organism.gety()
            biggerY = self.y
        else:
            smallerY = self.y
            biggerY = organism.gety()

        freeSpaces = []

        for i in range(smallerX, biggerX + 1):
            for j in range(smallerY, biggerY + 1):
                if(self.world.isFree(i, j)):
                    freeSpaces.append([i, j])

        if(len(freeSpaces) > 0):
            randomIndex = random.randint(0, freeSpaces.__len__() - 1)
            self.notMoved()
            organism.moveBack()
            self.world.addOrganism(self.id, self.animal, freeSpaces[randomIndex][0], freeSpaces[randomIndex][1])

    def collision(self, organism):
        if(self.id != organism.getId()):
            if(self.strength > organism.getStrength()):
                organism.kill()
                self.world.events.append("{} killed {}".format(self.name, organism.getName()))
            else:
                self.kill()
                self.world.events.append("{} was killed by {}".format(self.name, organism.getName()))
        else:
            self.spawnNewOrgnism(self, organism, self.world)

    def draw(self):
        return self.skin
