from pydantic import BaseModel

class user_query(BaseModel):
    query: str 
    filename: str 