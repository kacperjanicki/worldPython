
from cgitb import text
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
        user_data = self.query.get()
        newwin.title(f'size: {self.query.get()}')
        size=200*self.query.get()
        newwin.geometry(f"{100+int(size)}x{size}")
        
        # navigate to choose organism tooltip window
        def tooltip_win(pos):
            print(pos)
            self.chooseOrganism()
            
        root.withdraw()  ## hide main menu 
        display = Label(newwin, text="world size: " + self.query.get()) #getting parameter via query var
        world = World(self.query.get(), 2)
        label = Label(text='sample label')
        label.grid(row=int(self.query.get())+1,column=0)
        
        position_log=[]
        class Tile:
            def __init__(self, x,y):
                self.x = x
                self.y = y
            def button_command(self):
                self.button['text'] = 'x'
                if position_log.count((self.x,self.y)) < 1:      ##allows only one tooltip at the time (per tile)
                    tooltip_win((self.x,self.y))
                    position_log.append((self.x,self.y))
                
                print(position_log.count((self.x,self.y)))
                    

                    
            def create(self):
                self.button = Button(newwin,text='',command=self.button_command, height=5, width=5)
                self.button.grid(row=self.x,column=self.y)
        
        global event_log
        event_log = []   

        # tworzenie kafelkow
        for x in range(int(self.query.get())):
            for i in range(int(self.query.get())):
                Tile(0,i).create()
            for i in range(int(self.query.get())):
                Tile(x,i).create()

    def chooseOrganism(self):
        choose=Toplevel(root)
        choose.geometry('200x400')
        choose.title('Choose organism:')
        nazwy = ['Human','Antelope','Fox','Sheep','Turtle','Wolf','Belladona','Grass','Guarana','Sosnowsky Weed','Sow Thistle']

        def funkcja(i):
            wiadomosc = f"{i} has been added."
            print(wiadomosc)
            event_log.append(wiadomosc)
            print(event_log)

        # nie da sie tego zrobic for loopem (chyba)
        button1= Button(choose,text=nazwy[0],command=lambda: funkcja(nazwy[0]))
        button1.grid(row=0,column=0)
        button2= Button(choose,text=nazwy[1],command=lambda: funkcja(nazwy[1]))
        button2.grid(row=1,column=0)
        button3= Button(choose,text=nazwy[2],command=lambda: funkcja(nazwy[2]))
        button3.grid(row=3,column=0)
        button4= Button(choose,text=nazwy[3],command=lambda: funkcja(nazwy[3]))
        button4.grid(row=4,column=0)
        button5= Button(choose,text=nazwy[4],command=lambda: funkcja(nazwy[4]))
        button5.grid(row=5,column=0)
        button6= Button(choose,text=nazwy[5],command=lambda: funkcja(nazwy[5]))
        button6.grid(row=6,column=0)
        button7= Button(choose,text=nazwy[6],command=lambda: funkcja(nazwy[6]))
        button7.grid(row=7,column=0)
        button8= Button(choose,text=nazwy[7],command=lambda: funkcja(nazwy[7]))
        button8.grid(row=8,column=0)
        button9= Button(choose,text=nazwy[8],command=lambda: funkcja(nazwy[9]))
        button9.grid(row=9,column=0)
        button10= Button(choose,text=nazwy[9],command=lambda: funkcja(nazwy[9]))
        button10.grid(row=0,column=0)
        button11= Button(choose,text=nazwy[10],command=lambda: funkcja(nazwy[10]))
        button11.grid(row=10,column=0)

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