class Animal:
    def __init__(self , name):
        self.name = name 
    def info(self):
        print(f"I am a {self.name}")

class DOG(Animal):

    def __init__(self, name):
        super().__init__(name)

    def spec(self):
        print("Dog Barks ")
        

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
    def spec(self):
        print(f"I am a Cow and my name is : {self.name}")

d = DOG("Puppy")
d.info()
d.spec()

c = Cow("BOB")
c.info()
c.spec()