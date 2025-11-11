#problem 1 **************************

Num = 35
# reminder = Num % 2

# while reminder:
#     print(f"the reminder is : {reminder}")
#     break

# while ( reminder := Num % 2 ):
#     print(f"the reminder is : {reminder}")
#     break


#problem 2 ************************

# name = ["vivian" , "marcel" , "sequeira"]

# if req_name := input("enter the name that you want to search ") in name :
#     print("the name you searched is exist in her system ")
# else:
#     print("the name you searched don't exist in her system ")    


#problem 3 **************************

flovor = ["mango","tulsi","bannana","apple","choco"]
print(f"please select your Flovor {flovor}")

while (selected_flvr := input("select your flovor from the above ..")) not in flovor :
    print(f"the flovor {selected_flvr} is not available please select from {flovor}") 

print("thanks for choosing it ")    
