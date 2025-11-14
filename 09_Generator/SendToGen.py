
def orders():
    print("hey, Welcome ! what would you like to have ?")
    
    while True:
        order = yield
        print(f"the order #{order} is getting ready.")


cust_1 = orders()
next(cust_1)
cust_1.send("coffe")
cust_1.send("tea")

cust_2 = orders()
next(cust_2)
cust_2.send("Dosa")
cust_2.send("Pani Puri")
cust_2.send("Masala Dosa")