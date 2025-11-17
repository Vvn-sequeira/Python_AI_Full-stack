
class Chai:

    size = 130

    def describe(self):
        print(f"cup size is {self.size} ml")


cup = Chai() # Object of Chai class
cup.describe() # 130 ML

Chai.describe(cup) # 130 ML ( cup is a arg which will be cup = self )
 
cup2 = Chai() # Object of Chai class
cup2.size = 900 # cup2->size updated to 900ml

Chai.describe(cup2) # 900ml ( cup2 is a ref for the describe func)
Chai.describe(cup) # 130ml 
cup2.describe() # 900ml 