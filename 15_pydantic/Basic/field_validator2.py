from pydantic import BaseModel , field_validator

class age(BaseModel):

    age : int

    @field_validator('age')
    def validator(cls , a):
        if a <18: 
            print("You're Underage please exit.")
            return
        return a 
    
allowed = age(age=19)
print(allowed)

class Product(BaseModel):
    price : str 

    @field_validator('price' , mode='before')
    def Validate(cls , v):
        return v.replace('$','')
    

pricee = Product(price='$44.4')
print(f"Price is : {pricee.price}")
print(f"type of Price is : {(pricee.price)}")