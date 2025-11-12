
order = [23,34,46523,2]
print(f"Order before passing : {order}")
def change_the_val(set):
    set[2] = 0
    

change_the_val(order)
print(f"Order before passing : {order}")

# the list are Mutable 

#Kwargs

def chai(*argument , **extra):
    print(f"argumentss without any key value : {argument}")
    print(f"arguments with key value  : {extra}")


chai("coldcofee" , "cardmom" , sugar="medium" , size="big")