
# Dictionary 

Human = dict(name="vivian" , country="India" , State="Karnataka")
print(f"Info of Human : {Human}")

Student = {}

Student["name"] = "vivian"
Student["city"] = "Hassan" 
Student["college"] = "Aloysius" 

print(f"Student inof is : {Student}")
print(f"Student name is : {Student['name']}")

del Student['college']
# print(f"student college is : {Student['college']}") err

# membership
print(f"Is Sugar in the Order ? {'name' in Student}")


print(f"the keys are : {Student.keys()}")
print(f"the values are : {Student.values()}")




