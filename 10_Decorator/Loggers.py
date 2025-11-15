
from functools import wraps
def Loggers(func):
    @wraps(func)

    def Wrapper(*arg , **keywords):
        print(f"calling the function {func.__name__}")
        func(*arg , **keywords )
        print("completed the function")
    return Wrapper

@Loggers
def Brew_chai(type , milk="hot"):
    print(f"Brewing {type} chai , and milk is {milk}")

Brew_chai("Masala")