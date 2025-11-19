
class NOTFOUND(Exception): pass 

def PlaceAnOrder(flovor , cups):
    try:
         menu = {
        "Masala" : 20 ,
        "Ice coffe" : 40 , 
        "Juice" : 30
         }

         if flovor not in menu:
            raise ValueError("Please select it from our Menu!!")
    
         if not isinstance(cups , int):
            raise TypeError("please provide the NUmeric value for the qunatity")

         total = menu[flovor] * cups

         print(f"your Total Price is {total}")

    except Exception as e:
        print(f"Error: {e}")

PlaceAnOrder("cold Coffe" , 2)
PlaceAnOrder("Masala" , "3")
PlaceAnOrder("Masala" , 4)
