
class Details: # Class

    def __init__(self , name , from_ ): # ( __ init__ is a constructor ) (name & from_ are the parameters )
        self.name = name  # self.name -> it creates a varible "name" 
        self.from_ = from_

    def details(self): # Method to print the details
        return f"{self.name} is from {self.from_}"
    

info = Details("Vivian" , "Hassan ") # info -> it is a obj 

print(info.details())
