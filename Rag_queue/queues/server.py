from fastapi import FastAPI 

app = FastAPI() 

@app.get("/")
def root():
    return {"Status": "server is Running"} 