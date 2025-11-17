
class GrandParent():
    def __init__(self , name):
        self.name = name

    def Gintro(self):
        print(f"I am Grand Parent and my name is : {self.name}")

class Parent(GrandParent):
    def __init__(self, Gname , Pname):
        super().__init__(Gname)
        self.Pname = Pname
    
    def Pintro(self):
        super().Gintro()
        print(f"I am  Parent and my name is : {self.Pname}")

class Child(Parent):
    def __init__(self, Gname, Pname , Cname):
        super().__init__(Gname, Pname)
        self.Cname = Cname

    def Cintro(self):
        super().Pintro()
        print(f"I am Grand Parent and my name is : {self.Cname}")

Family =  Child("BOB" , "DOB" , "ROB")
Family.Cintro()



