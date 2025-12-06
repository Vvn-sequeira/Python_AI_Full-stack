
Max = int(input("Enter the maximum Stars : "))

for i in range(1,10):
    if i <= Max:
       print("X"*i)
    else:
        Max -= 1
        print("X"*Max)

    