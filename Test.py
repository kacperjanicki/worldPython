class Test:
    def __init__(self):
        self.organisms = []
        self.events = []
        self.human = None
    
    def turn(self):
        self.organisms[0].collision(self.organisms[1])
