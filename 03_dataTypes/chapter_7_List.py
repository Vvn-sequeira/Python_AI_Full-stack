
# List are Array 

names = ['vivian', 'marcel']
names.append("sequeira")

print(f"Names are : {names}")

names.remove("vivian")
print(f"Names are : {names}") 

nations =['india','china','USA']

#Extend
names.extend(nations);
print(f"Names are : {names}")


#insert 
names.insert(2 , "Raja");
print(f"Names are : {names}")

# Pop
last_added = names.pop();
print(f"last addded : {last_added}")

# Reverse 

names.reverse();
print(f"Names are in reverse formate : {names}")

# Sort
print(f"Sort the names  : {names}")


# max and min
Sugar_level = [1,2,3,4,5,5,6]
print(f"Max : {max(Sugar_level)}")
print(f"min : {min(Sugar_level)}")


# Operator overloading 

val1 =[1,2,3]
val2 = [5,6]

finalVal = val1 + val2
print(f"final val : {finalVal}")

val3 = [2]
print(f"val3 time 3 : {val3 * 3}")