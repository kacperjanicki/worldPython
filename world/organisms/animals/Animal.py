
import random
from world.organisms.Organism import Organism


class Animal(Organism):
    def __init__(self, world):
        super().__init__(world)
        self.animal = True

    def move(self):
        if(random.random() < 0.5):
            if(random.random() < 0.5):
                if(self.x < self.world.size - 1):
                    self.x += 1
                else:
                    self.x -= 1
            else:
                if(self.y < self.world.size - 1):
                    self.y += 1
                else:
                    self.y -= 1
        else:
            if(random.random() < 0.5):
                if(self.x > 0):
                    self.x -= 1
                else:
                    self.x += 1
            else:
                if(self.y > 0):
                    self.y -= 1
                else:
                    self.y += 1

    def action(self):
        if(self.alive):
            self.move()
