from datetime import date 

d,m,y= map(int, input("Enter Day , Month , Year").split("/"))

issueDate = date(y,m,d)
returnDate = date.today() 

Days = (returnDate - issueDate).days

print(f"{Days} : Days ")
fine = 0 


if Days<=15:
    fine=0 
elif Days <=20: 
    fine = (Days - 15)*0.05 
elif Days <=25: 
    fine = 5*0.05 + (Days - 20)*1 
elif Days <=30: 
    fine = 5*0.05 + 5 + (Days - 25)*5
else: 
    print("Sorry Your Membership is Cancelled!")
    
    
if fine == 0 : 
    print("Thank You for coming Visit Again ")
else : 
    print(f"Pay Fine of {fine}rs ")