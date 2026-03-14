from pydantic import BaseModel 
from datetime import datetime
from typing import List


class ChatMessage(BaseModel):
    user: str 
    RAG: str 
    time: datetime = datetime.now() 


class Chat(BaseModel):
    user_id: str  
    sender_name: str
    receiver_name: str
    message: List[ChatMessage] = []
    
    
#     {
#   "user_id": "string",
#   "sender_name": "vivian",
#   "receiver_name": "seq",
#   "message": [
#   {
#     "user": "hello seq",
#     "RAG": "Hey vivian" 
#   } 
# ]
# }