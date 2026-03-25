from fastapi import FastAPI , Query
from client.rq_client import queue
from queues.query import get_result
import multiprocessing
app = FastAPI() 

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    


@app.get("/")
def root():
    return {"Status": "server is Running"} 

@app.post("/Chat")
def chat( query: str = Query(..., description="The chat query of User")):
    job = queue.enqueue(get_result, query) 
    return {"Status":"Queued" , "Job_id": job.id }