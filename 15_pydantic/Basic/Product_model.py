from pydantic import BaseModel

class Product(BaseModel):
    id: int 
    name:str
    price:float 
    in_Stock:bool = True


product1 = Product(id=1 , name="Laptop" , price=999.44 , in_Stock=True)

product_2 = Product(id=2 , name="Mouse" , price=24.99 )

product_3 = Product(id=3 , name="keyboard"  ) # field required 