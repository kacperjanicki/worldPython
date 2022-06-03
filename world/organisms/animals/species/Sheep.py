
from world.organisms.animals.Animal import Animal


class Sheep(Animal):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Sheep"
        self.skin = "S"
        self.id = 2
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 4
        self.baseStrength = 4
        self.initiative = 4
