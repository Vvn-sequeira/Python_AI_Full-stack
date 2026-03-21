l = int(input("Enter Lower Limit"))
u = int(input("Enterrr Upper Limit"))

for i in range(l,u+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:       
        print(f" {i} is A Prime NO. ")
    
    