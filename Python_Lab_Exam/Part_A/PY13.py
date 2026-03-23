import numpy as np

row , col = map(int, input("Enter ROW and COL ").split())

arr1 = np.zeros((row,col),int)
arr2 = np.zeros((row,col),int)

#enter value 
for i in range(row):
    for j in range(col): 
        arr1[i][j] = int(input("Enter Value for Array 1 : "))

for i in range(row):
    for j in range(col):
        arr2[i][j] = int(input("Enter Value for Array 2 : "))

add_matrix = np.add(arr1 , arr2 )
sub_matrix = np.subtract(arr1 , arr2 )

print(f"The Array 1: {arr1}")
print(f"\n\nThe Array 2: {arr2}")


print(f"\n\nThe Array after Adding to the array 2 : {add_matrix}")
print(f"\n\nThe Array after Substracting with  array 2 : {sub_matrix}")


