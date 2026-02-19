from fastapi import FastAPI
from auth import HashPass , verifyPass , create_access_JWT , SignUp , LogIn
from Modles.User_Modles import User_info , User_register , User_login
app = FastAPI() 


@app.get("/")
def hello():
    return {"message": "Hello there!"}


@app.post("/api/auth/signup")
def sigUp(register:User_register):
    token = SignUp(register=register)
    return {"data": "Successfully registered " , "token": token}

@app.post("/api/auth/login")
def login(login:User_login):
    res = LogIn(login) 
    return {"res": res }