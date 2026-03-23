from abc import ABC , abstractmethod

class Turism(ABC):
    Rent_HOUSE = 2500
    Rent_Vehical = 40 
    
    def __init__(self, name): 
        self.name = name 
        
    @abstractmethod
    def billingDetails(self, value):
        pass 
    
class HouseRent(Turism):
    def __init__(self, name , NO_gh):
        super().__init__(name)
        self.No_gh = NO_gh 
        
    def billingDetails(self, value):
        self.No_Days = value
        print(f"custName {self.name}")
        print(f"Nummber of Guest :  {self.No_gh}")
        print(f"Nummber of Days :  {self.No_Days}")
        print(f"Toatal Amount : {self.Rent_HOUSE * self.No_Days }")

class VechicalRent(Turism):
    def __init__(self, name):
        super().__init__(name)
        
    def billingDetails(self, value):
        self.No_km = value 
        print(f"Cust Name : {self.name}")
        print(f"No of Km : {self.No_km}")

        if self.No_km < 20:
            self.amt = 20 * self.Rent_Vehical
        else: 
            self.amt = self.No_km * self.Rent_Vehical   
            
        print(f"Toatal cost : {self.amt}")


name = input("Enter the name : ")
No_gh , No_days , No_km = map(int , input("Enter no of Guest | no of Days | no of Km ").split())

h = HouseRent(name , No_gh )
h.billingDetails(No_days)

v = VechicalRent(name)
v.billingDetails(No_km)

