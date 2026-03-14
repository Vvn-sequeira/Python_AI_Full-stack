from fastapi import Request , HTTPException , status
from starlette.middleware.base import BaseHTTPMiddleware
from jose import jwt , JWTError 
from DatabaseConnect import client
from Modles.User_Modles import User_info

DB = client['User_INFO']
user_collection = DB["User_Login"]


SECRET_KEY='DJFALJD'
ALGORITHM='HS256'

class authMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request:Request, call_next):
        
        token = request.cookies.get("access_token")
        
        if token:
            try:
                payload = jwt.decode(token ,SECRET_KEY ,ALGORITHM)
                request.state.user = payload
                
            except JWTError:
                raise HTTPException(status_code=401, detail="Invalid token")
        response = await call_next(request)
        return response 
    
    
    
class authVerify(BaseHTTPMiddleware):
    async def dispatch(self , request:Request , call_next ):
        
        if request.url.path in ["/api/auth/signup", "/api/auth/login"]:
            return await call_next(request)
        print("⚠️⚠️",request.url.path)
        token = request.cookies.get("access_TOKEN")
        if not token:
            raise HTTPException(status_code=401, detail="Token missing")

        if token:
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                email = payload.get("email")
                user_id = payload.get("user_id")
                exist = user_collection.find_one({"email":email})
                print("🌹🌹🌹🌹",exist)
                if not exist:
                    raise HTTPException(status_code=401, detail="User not found")
                request.state.user = exist    
                request.state.user_id = user_id    
            except Exception as e:
                raise e 
            except JWTError: 
                 raise HTTPException(status_code=404, detail="NOT ALLOWED TO ACCESS") 
        response = await call_next(request)
        
        return response