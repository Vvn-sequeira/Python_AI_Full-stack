from fastapi import FastAPI , Response , status , HTTPException , Request
from auth import HashPass , verifyPass , create_access_JWT , SignUp , LogIn
from Modles.User_Modles import User_info , User_register , User_login
from Modles.ChatModule import Chat , Chat_access
from Middlewares.AuthMiddleware import authMiddleware , authVerify
from Modles.AI_assis import user_query
from Modles.get_req import get_req
from ChatRoute import ChatReply , View_messages
from send_req_Route import Push_req
from RAG_Model.FILE_RETRIVEL import Vector_search
from fastapi.middleware.cors import CORSMiddleware
from DatabaseConnect import client
app = FastAPI() 
# app.add_middleware(authMiddleware)

DB = client['User_INFO']
user_collection = DB["User_Login"]

# app.add_middleware(authVerify)

origins = ["http://localhost:3000" ,"http://192.168.56.1:3000" , "http://10.174.123.56:3000" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"message": "Hello there!"}


@app.post("/api/auth/signup", status_code=status.HTTP_200_OK)
def sigUp(register: User_register, res: Response):

    token = SignUp(register)

    res.set_cookie(
        key="access_TOKEN",
        value=token,
        httponly=True,
        secure=True,
        samesite="none",
        path='/'
    )

    return {"message": "Successfully registered" }


@app.post("/api/auth/login", status_code=status.HTTP_200_OK)
def login(login:User_login , res:Response ):
    
    token = LogIn(login) 
    
    res.set_cookie(
        key="access_TOKEN",
        value=token,
        httponly=True,
        secure=True,
        samesite="none",
        path='/'
    )
    
    return {"message" :"User Logged IN successfully !!"}


@app.post("/api/agent")
def agent_reply(query:user_query):
    res = Vector_search(query.filename , query.query) 
    return {"res": res}


@app.post("/api/Chat" , status_code=status.HTTP_200_OK )
def savechat(chats: Chat , request: Request  ):
    # id = request.state.user_id 
    id = "69b571798356e36c325c8505"
    
    return ChatReply(chats , id ) 


@app.post("/api/view" , status_code=status.HTTP_200_OK)
def viewChat(data:Chat_access , request: Request):
    user_id = request.state.user_id 
    res = View_messages(data.receiver_name , user_id)
    return {"res": res }


@app.post("/api/getreq", status_code=status.HTTP_200_OK)
def ret_req_from_user(data:get_req , request:Request ): 
    res = Push_req(data)
    
    return {"message": f"Done Inserting ONE : {res} "}