import array

arr = array.array("i")

n = int(input("Entert the max size "))

for i in range(n):
    ele = int(input(f"Enter the ele for the Index {i}"))
    arr.append(ele)
    
Menu = """
1. Add New ELE 
2. Insert at NEW Position 
3. Remove ele 
4. Sort in Reverse order value 
5. Print array 
6. Exit 
"""
while True: 
    print(Menu)
    ch = int(input("Enter your choice? "))

    if ch == 1: 
        ele = int(input("Enter the New ele to be added "))
        arr.append(ele)

    elif ch == 2: 
        ele,pos = map(int , input("Enter Ele and Pos").split())
        arr.insert(pos , ele  )

    elif ch == 3: 
        ele = int(input("Enter the ele to be Removed "))
        arr.remove(ele )

    elif ch == 4 : 
        b = sorted(arr)
        b = reversed(b)
        for i in b :  
            print(i, end="")
        
    elif ch == 5: 
        print(arr)

    else: 
        print("Exiting the prg!!")
        break 