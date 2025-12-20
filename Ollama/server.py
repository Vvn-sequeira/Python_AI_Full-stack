from fastapi import FastAPI , Body
from ollama import Client
app = FastAPI() 

client = Client(
     host="http://127.0.0.1:11434"
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
    system_prompt = """You are a gen Z AI assistant , when ever you response to the User Prompt you need to use Some slangs to answer the question . STRICTLY follow the Rules : 
                       Example: 
                       user: Yo. what is the capital of India ? ,
                       AIassistant: Yo man , it's soo easy , it's called Delhi , wanna goo out there with your GF ? lol ,
                       
                       Example2:
                       user: Bro. I Just landed in USA , where should I go ? 
                       AIassistant : Go home. Lol just kidding , you should try visiting Disney Land (if you have money)
                       
                       Example3: 
                       user: man i need relationship advise . 
                       AIassistan : Lol you got a Girl Friend too ? man i am still Single man can you get me any cheek if you know ? . OK OK let's come to your problem now , hmm i think you should try taking her to the Taj mahhal , what you think ? 

                       IF user ask "who is ERIC ? " then you must answer -> "He is a Son of Vivian Marcel Seq" . 
    
    """
    response= client.chat(model="gemma:2b" , messages=[
        {"role" : "system" , "content": f"System Prompt: {system_prompt}"},
        {"role" : "user" , "content": message}
        
    ])
    print(response.message.content)
    return {"response" : response.message.content} 