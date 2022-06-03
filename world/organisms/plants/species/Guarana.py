
from world.organisms.plants.Plant import Plant


class Guarana(Plant):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Guarana"
        self.skin = "G"
        self.id = 3
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 0
        self.baseStrength = 0

    def collision(self, organism):
        self.kill()
        organism.strength += 3