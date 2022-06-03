
import pygame
from world.World import World


world = World(20, 2)
world.addHuman(5, 5)
world.human.usePotion()
world.saveToFile("test3.txt")

# masz dostępne:
#     world = World(WorldSize, spawnProtectSize)    WorldSize musi być ustalany w oknie przed rozpoczęciem gry, spawnprot zostaw 2 i es
#     world.makeTurn()
#     world.saveToFile("saveFile.txt")
#     world.loadFromFile("saveFile.txt")
#     world.populate()                  przy odpaleniu nowej gry trzeba odpalić żeby jakieś organizmy tam były
#     world.addOrganism()
#     world.events                      lista eventów, możesz wyświetalć gdzieś w oknie np 5 ostatnich albo tak jak ja w java
#                                           że nowe okno z całą listą i elo

#     strzałkami klawiatury można ustalić kierunek ruchu         po odpaleniu nowej tury ziom juz sam sobie bedzie chodził
#     world.human.setDirectionX(INT)
#     world.human.setDirectionY(INT)
#     world.human.usePotion()

#     klikając na daną komórkę świata można dodać organizm (tak jak w javie, że lista się pokazuje)
#     masz do tego w world funkcje:
#     addHuman(x, y)
#     addWolf(x, y)
#     addSheep(x, y)
#     addFox(x, y)
#     addTurtle(x, y)
#     addAntelope(x, y)
#     addCyberSheep(x, y)
#     addGrass(x, y)
#     addSowThistle(x, y)
#     addGuarana(x, y)
#     addBelladona(x, y)
#     addSosnowskyHogweed(x, y)