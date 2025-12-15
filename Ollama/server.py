from fastapi import FastAPI , Body
from ollama import Client
app = FastAPI() 
client = Client(
    host="http://127.0.0.1:8000"
)

@app.get("/")
def read_root():
    return {"Hello" : "World"}
@app.get("/contact")
def read_root():
    return {"Email" : "svivian@gmail.com"}

@app.post("/chat")
async def chat(
    message : str = Body(..., description="The message")
):
    response= await client.chat(model="gemma:2b" , messages=[
        {"role" : "user" , "content": message}
    ])
    
    return {"response" : response.message.content} 