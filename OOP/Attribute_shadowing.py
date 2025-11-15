
class Chai:
    temperature = "hot"
    strenght = "Strong"

cutting = Chai() # OBject

cutting.temperature = "Mild"
cutting.price = 128
print(cutting.temperature) 
print(cutting.price) 

del cutting.temperature
del cutting.price

print(cutting.temperature)
print(cutting.price)
