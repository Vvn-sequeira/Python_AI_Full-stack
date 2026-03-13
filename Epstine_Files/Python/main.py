from fastapi import FastAPI
from fastapi import Response , status , Request
from auth import HashPass , verifyPass , create_access_JWT , SignUp , LogIn
from Modles.User_Modles import User_info , User_register , User_login
from Middlewares.AuthMiddleware import authMiddleware , authVerify
from Modles.AI_assis import user_query
from RAG_Model.FILE_RETRIVEL import Vector_search
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI() 
# app.add_middleware(authMiddleware)
# app.add_middleware(authVerify)

origins = [
    "http://localhost:3000",   # React / Next.js
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.post("/api/agent")
def agent_reply(query:user_query):
    res = Vector_search(query.filename , query.query) 
    return {"res": res}