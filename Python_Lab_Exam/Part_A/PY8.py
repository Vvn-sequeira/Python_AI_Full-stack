st_info = {}

n = 3
print("(((((((Enter Student INFO)))))))")
for i in range(1,n+1):
    reg = int(input("Enter st reg ")) 
    name = input("Eter name ")

    st_info[reg] = name 
    
find_reg = int(input("Enter the reg to find "))


if find_reg in st_info: 
    print("Student Exist!")
    print(f"Register NO is : {find_reg}")
    print(f"Name is : {st_info[find_reg]}")


    
