from pydantic import BaseModel , EmailStr
from typing import Optional


class User_login(BaseModel):
    user_name: str 
    email:EmailStr
    password:str 
    
    
class User_register(BaseModel):
    user_name: str 
    email:EmailStr
    phoneNo:str
    password:str 
    token: int = 4
    
    
class User_info(BaseModel):
    user_name: str 
    email:EmailStr
    phoneNo:str
    token: int = 4  