
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

# Pop the ele for the dict
last_item = Human.popitem()
print(f"last item of humna DIct is : {last_item}")
print(f"after Poped the ele  : {Human}")

# Update the ele for the dict 
updated_Human = {"name" :"Marcel" , "country" : "India" , "State" : "Delhi"}
Human.update(updated_Human);
print(f"Human : {Human}");

# CityofHuman = Human["City"]
# print(f"City of human {CityofHuman}")

StateOfHuman = Human.get("City" , "No info of State ");
print(f"State of Human {StateOfHuman}")


# Sets Operation 
#Human = dict(name="vivian" , country="India" , State="Karnataka")
# Student["name"] = "vivian"
# Student["city"] = "Hassan" 

UnionDict = Human | Student
print(f"Uniion of two Data set {UnionDict}")