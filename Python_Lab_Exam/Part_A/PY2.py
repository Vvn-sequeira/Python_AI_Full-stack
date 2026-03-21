n = int(input("Enter Max Star"))


for i in range(1 , n*2): 
    
    if i < n : 
        print("*"*i, end="")
        print() 
    else:
        n-=1 
        print("*"*n , end="")
        print() 