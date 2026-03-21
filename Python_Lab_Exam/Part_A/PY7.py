OT_PaY = 0 

worker_dict ={}

for i in range(1,5): 
    hours= int(input(f"Enter the Hourse worked by worker : {i}"))

    if hours > 40 : 
        OT_PaY = (hours - 40 )* 12
    else:
        OT_PaY = 0 
        
    worker_dict[i] = (hours,OT_PaY)
    
print("\t EmP_NO \t EMP_WORKING_HOURS \t EMP_OT_PAY ")
for i , emp in worker_dict.items(): 
    print(f"\t {i} \t\t {emp[0]} \t\t\t {emp[1]}")