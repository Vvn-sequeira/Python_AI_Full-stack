
from functools import wraps
def auth_deco(func):
    @wraps(func)

    def Wrapper(role):
        if(role != "admin"):
             print("You are not Admin!!")
             return None 
        else:
         return func(role)
    return Wrapper

@auth_deco
def admin_page(role):
    print("welcome admin!!!")

admin_page("user")