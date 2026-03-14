from DatabaseConnect import client 
from fastapi import status , HTTPException , Response , Request
import os 
# from json import jwt 
from fastapi.middleware.cors import CORSMiddleware
from Modles.ChatModule import Chat
from Modles.User_Modles import User_info 
from bson import ObjectId
from RAG_Model.FILE_RETRIVEL import Vector_search
DB = client['User_INFO']
chat_collection = DB['Chat_collection']
user_collection = DB['User_Login']


def ChatReply(chats:Chat , user_id):
    
    try:
        exist = chat_collection.find_one({"user_id": user_id , "receiver_name": chats.receiver_name })
        
        res = Vector_search(chats.receiver_name , chats.message[0].user )
        
        msg = {
            "user": chats.message[0].user,
            "RAG": res
        }
        
        if not exist: 
                chat_collection.insert_one({
                "user_id": user_id  ,
                "sender_name": chats.sender_name ,
                "receiver_name": chats.receiver_name ,
                "message": [msg] ,
            })
        else: 
            chat_collection.update_one(
                {"user_id": user_id , "receiver_name": chats.receiver_name}, {"$push": {"message": msg }}
            )
    except Exception as e : 
        raise e
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong!"
        )  
        
    