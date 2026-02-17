from fastapi import FastAPI
from pydantic import BaseModel
from models import user_inp
from database import collection 
from fastapi.middleware.cors import CORSMiddleware


from Ai import AiAgentReply
app = FastAPI() 


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Hello my friend!"}


@app.get("/sayHI/{name}")
def Say_HI(name:str):
    return {f"greetings":f"{name}, GOOD MORNING!"}


# query parameter 
@app.get("/search")
def search(q:str):
    return {"HMMM I found your ": f"{q}"}

class User(BaseModel):
    name:str 
    age:int 
    
    
@app.post("/user_login")
def login(users : User):
    return {f"Username:{users.name} | UserAge: {users.age }"}

@app.post("/signUp")
def signup(user:user_inp):
    user_dict = user.model_dump() 
    collection.insert_one(user_dict)
    print("Successfully Inserted!!!")
    
    
@app.post("/AiAgent")
def Call_agent(query:str):
    res = AiAgentReply(query)
    return res 