from fastapi import FastAPI
from fastapi import Response , status , Request
from auth import HashPass , verifyPass , create_access_JWT , SignUp , LogIn
from Modles.User_Modles import User_info , User_register , User_login
from Middlewares.AuthMiddleware import authMiddleware , authVerify

app = FastAPI() 
app.add_middleware(authMiddleware)
app.add_middleware(authVerify)



@app.get("/")
def hello():
    return {"message": "Hello there!"}


@app.post("/api/auth/signup")
def sigUp(register:User_register , res:Response):
    token = SignUp(register=register)
    res.set_cookie(
        key="access_TOKEN",
        value=token,
        httponly=True,
        secure=True,
        samesite="lax"
    )
    return {"data": "Successfully registered "}, status.HTTP_200_OK

@app.post("/api/auth/login")
def login(login:User_login):
    res = LogIn(login) 
    return {"res": res }