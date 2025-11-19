
def process_order(item , quantity):

    try: 
         price = {
          "Masala" : 20 , 
          "Ice cofee": 40 , 
          "Coffe" : 25
         }[item]

         cost = quantity * price 
         print(f"Total is : {cost}")
        
    except KeyError:
         print("Please choose from the menu !!")
    except TypeError:
         print("Qunatity must be in a Numeric ")


process_order("Masala" , 3) 
process_order("hello" , 3) 
process_order("Coffe" , "Three") 

