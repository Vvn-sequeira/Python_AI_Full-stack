from passlib.context import CryptContext
from jose import jwt 
from fastapi import status , HTTPException , Response
from pydantic import BaseModel
from datetime import datetime , timedelta
from DatabaseConnect import client
from Modles.User_Modles import User_register, User_info , User_login
from fastapi.middleware.cors import CORSMiddleware 
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

def SignUp(register: User_register):

    user = user_collection.find_one({"email": register.email})

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists!"
        )

    register_dict = register.model_dump()

    register_dict["password"] = HashPass(register.password)

    new_user = user_collection.insert_one(register_dict)

    print("DONE!! User successfully registered!!")

    token = create_access_JWT({
        "email": register.email,
        "user_id": str(new_user.inserted_id)
    })

    return token

def LogIn(LogIn:User_login ):
    try:
        exist = user_collection.find_one({"email":LogIn.email}) 
        if exist:
            valid = verifyPass(LogIn.password , exist['password']  ) 
            print(valid)
            if valid:
                token = create_access_JWT({"email": exist['email'], 'user_id': str(exist['_id']) })
                return token
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email or Password is Not valid , Please check once and try again!!" 
                )
                
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User Not found! Please SignUp.."
            )
    except Exception as e:
        raise e 
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong from our Side , please try again later.. "
        ) 
    
    
