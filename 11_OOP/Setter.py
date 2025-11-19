
class DrivingLic:

    def __init__(self , age):
        self._age = age 
    @property
    def _age(self):
        return self._age 

    @_age.setter
    def _age(self , age):

        if age <=17 :
           raise ValueError("You need to be an Adult!!")
        else:
            print(f"Congragulation , you will get your DL soon") 

DL = DrivingLic(12)

print(DL)
