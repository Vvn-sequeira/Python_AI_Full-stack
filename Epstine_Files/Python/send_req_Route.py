from DatabaseConnect import client
from Modles.get_req import get_req
DB = client["User_INFO"]
req_collection = DB['req_from_user']


def Push_req(data:get_req):
    data = data.model_dump()
    done = req_collection.insert_one(data)
    return done  
    