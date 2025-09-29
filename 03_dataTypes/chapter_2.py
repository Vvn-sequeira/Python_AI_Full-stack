# Mutable

cars_name = set() ; # set is a data type which is Mutable 
print(f"Initial cars_name : (cars_name)")
print(f"Initial cars_name id : {id(cars_name)}")

cars_name.add("Buggati Veyron") ;
print(f"Second cars_name : {cars_name}")
print(f"Second cars_name id : {id(cars_name)}")

cars_name.add("Alto");
print(f"Second cars_name : {cars_name}")
print(f"Second cars_name id : {id(cars_name)}")
