li =  [500,400,300,200,100]

amt = int(input("Enter the Amount please "))

if amt % 100 == 0:
    for i in li:
        if amt == 0:
            break
        print(f"{i} : {amt/i} Notes")
        amt = amt - (amt/i)*i 
        