from fastapi import Request , HTTPException , status
from starlette.middleware.base import BaseHTTPMiddleware
from jose import jwt , JWTError 
from DatabaseConnect import client
from Modles.User_Modles import User_info
from starlette.responses import JSONResponse

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
    async def dispatch(self, request: Request, call_next):
        
        if request.url.path in ["/api/auth/signup", "/api/auth/login"]:
            return await call_next(request)

        token = request.cookies.get("access_TOKEN")
        print("🔪🔪🔪Token: ", token)

        if not token:
            return JSONResponse(   
                status_code=401,
                content={"detail": "Token missing"}
            )

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email = payload.get("email")
            user_id = payload.get("user_id")
            exist = user_collection.find_one({"email": email})

            if not exist:
                return JSONResponse(  
                    status_code=401,
                    content={"detail": "User not found"}
                )

            request.state.user = exist    
            request.state.user_id = user_id    

        except JWTError:
            return JSONResponse(  
                status_code=401,
                content={"detail": "NOT ALLOWED TO ACCESS"}
            )

        response = await call_next(request)
        return response
