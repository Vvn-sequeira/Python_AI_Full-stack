import random 

number = []

n = int(input("Enter Max size "))

for i in range(n): 
    number.append(random.randint(1,5))
    
print(f"the List is : {number}")

count_dict = {}
for i in number: 
    count_dict[i] = number.count(i)
    
    
print(f"the counting Dictionary ! ")
print(count_dict)

