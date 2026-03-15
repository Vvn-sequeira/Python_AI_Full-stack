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
        print(chats)
        exist = chat_collection.find_one({"user_id": user_id , "receiver_name": chats.receiver_name })
        user = user_collection.find_one({"_id":ObjectId(user_id)})
        
        if not user: 
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User doesn't Exist , Please Login through Our WebSite.. "
            )
        token = user['token']
        
        if token <= 0:
            raise HTTPException( 
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="You have reached you Token Limit."
            )
            
        print(user)
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
            
       
        token -= 1
        user_collection.update_one({"_id":ObjectId(user_id)} , {"$set": {"token": token}})
        
        return res 
    except Exception as e : 
        raise e
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong!"
        )  
        
    
    
def View_messages(rec_name , id ):
    
    try: 
        user_id = id
        
        get_msg = chat_collection.find_one({"user_id": user_id , "receiver_name": rec_name})
        
        if not get_msg:
            return 
        
        print(get_msg)
        
        return get_msg['message']
    except Exception as e:
        raise e 