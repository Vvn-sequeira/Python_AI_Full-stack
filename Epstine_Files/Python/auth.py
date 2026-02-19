from passlib.context import CryptContext
from jose import jwt 
from pydantic import BaseModel
from datetime import datetime , timedelta
from DatabaseConnect import client
from Modles.User_Modles import User_register, User_info , User_login

SECRET_KEY='DJFALJD'
ALOGRITHM='HS256'

DB = client['User_INFO']
user_collection = DB["User_Login"]

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

#Hash the Pass
def HashPass(password:str):
    return pwd_context.hash(password)

#Verify Password
def verifyPass(req_pass,real_pass):
    return pwd_context.verify(req_pass, real_pass)

# create JWT token 
def create_access_JWT(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=4)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALOGRITHM)

def SignUp(register:User_register):
    register_dict = register.model_dump() 
    register_dict['password'] = HashPass(register.password)
    Token = create_access_JWT({"email":register.email})
    user_collection.insert_one(register_dict)
    print("DONE!! User successfully registerd!! ")
    return Token

def LogIn(LogIn:User_login):
    exist = user_collection.find_one({"email":LogIn.email})
    
    if exist:
        valid = verifyPass(LogIn.password , exist['password']  ) 
        if valid:
            pass 
        else:
            return {"error" : "Email or Password is Not valid , Please check once and try again!! "}
    else: 
        return {"error": "the Account doesn't exist in DB , pleases signUp"}
         
    token = create_access_JWT({"email": exist['email']})
    
    return {"message" : "DONE!!" , "TOKEN": token}