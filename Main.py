
import tkinter
# import pygame
from world.World import World
import tkinter as tk
from tkinter import *
# from tkinter import simpledialog       tym mozna miec dialog window jak w javie
#                                        ale nie wiem jak przez query to wyslac
                                    # data=simpledialog.askstring(title='input',prompt='world size')
                                    # print(data)

class Frames(object):
    def newFrame(self):
        newwin = Toplevel(root)
        newwin.title(f'size: {self.query.get()}')
        size=200*self.query.get()
        newwin.geometry(f"{100+int(size)}x{size}")
        screen_height = newwin.winfo_reqheight()
        screen_width = newwin.winfo_reqwidth()
        print(screen_width,screen_height)

         
        root.withdraw()  ## hide main menu 

        display = Label(newwin, text="world size: " + self.query.get()) #getting parameter via query var

        world = World(self.query.get(), 2)

        class Tile:
            def __init__(self, x,y):
                self.x = x
                self.y = y
            def button_command(self):
                print(self.x,self.y)
            
            def create(self):
                self.button = Button(newwin,command=self.button_command, height=5, width=5)
                self.button.grid(row=self.x,column=self.y)

        
        # tworzenie kafelkow
        for x in range(int(self.query.get())):
            for i in range(int(self.query.get())):
                Tile(0,i).create()
            for i in range(int(self.query.get())):
                Tile(x,i).create()


            




    def mainFrame(self,root):
        self.query = StringVar() #passing parameter via query var
        
        def click():
            if len(self.query.get()) == 0:
                print('error')
            else:
                self.newFrame()
        
        root.title('Main win')
        root.geometry("300x300") 
        root.resizable(0, 0)
        
        label = Label(root,text='Give world size:')
        label.grid(row=0,column=0)
        
        button1 =Button(root, text ="New game", command =click)
        button1.grid(row=1,column=1)

        entry1 = Entry(root, textvariable=self.query)
        entry1.grid(row=1,column=0)
        

if __name__ == "__main__":
    root = Tk()
    app = Frames()
    app.mainFrame(root)
    root.mainloop()


# world = World(20, 2)
# world.addHuman(5, 5)
# world.human.usePotion()
# world.saveToFile("test3.txt")




# masz dostępne:
#     world = World(WorldSize, spawnProtectSize)    WorldSize musi być ustalany w oknie przed rozpoczęciem gry, spawnprot zostaw 2 i es
#     world.nextTurn()
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