from database import collection
from pydantic import BaseModel

class user_inp(BaseModel):
    name:str 
    age:int
    password:str 
    
    
