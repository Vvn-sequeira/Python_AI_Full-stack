
snak = input("What's you want to order ? : ").lower()

if snak == "soda" or snak == "juice" or snak == "chai": 
    print(f"yes available ")
else:
    print(f"Sorry! it's Unavailable ...")    

cup_size = input("Please Select your Cup Size (Small : 10rs | Medium : 15rs | Large : 20 )").lower()

if cup_size == "small":
    print(f"Thank you for choosing it and your order Total is : {30}")
elif cup_size == "medium": 
    print(f"Thank you for choosing it and your order Total is : {35}")
elif cup_size == "large" : 
    print(f"Thank you for choosing it and your order Total is : {40}")
else : 
    print(f"Invalid Cup size !! ")