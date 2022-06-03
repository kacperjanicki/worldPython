
from world.organisms.plants.Plant import Plant


class Grass(Plant):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Grass"
        self.skin = "."
        self.id = 1
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 0
        self.baseStrength = 0