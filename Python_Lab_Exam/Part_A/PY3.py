amt = int(input("Enter the amount "))

if amt%5 != 0 : 
    print("Amt is Not denomination of 5")
else: 
    for i in [500 , 100 , 50 , 10 , 5]: 
        print(f"{amt//i} : {i} NOTES ")
        amt = amt%i 