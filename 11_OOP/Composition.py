
class Engine:
    
    def Start(self):
        print("Engine Started")

class Bettery:

    def Charge(self):
        print("Battery Charged")

class Car:

    def __init__(self):
        self.E = Engine()
        self.B = Bettery()

    def On(self):
        self.E.Start()
        self.B.Charge()
        print("Card is ready to GOOOO")

C = Car()
C.On()