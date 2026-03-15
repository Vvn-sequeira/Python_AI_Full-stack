from pydantic import BaseModel 


class get_req(BaseModel):
    email: str 
    user_name: str 
    doc_Link: str 
    reason: str 