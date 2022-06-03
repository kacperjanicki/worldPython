
from world.organisms.plants.Plant import Plant


class Belladona(Plant):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Belladona"
        self.skin = "B"
        self.id = 4
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 99
        self.baseStrength = 99