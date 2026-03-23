def fact(i):
    if i <= 0: 
        return 1
    else : 
        return i*fact(i-1)
    
    
lis = [] 

for i in input().split():
    lis.append(int(i))   
    

fac = list(map(fact , lis ))

print(f"The List is : {lis}")
print(f"The Factorial of the List is : {fac}")