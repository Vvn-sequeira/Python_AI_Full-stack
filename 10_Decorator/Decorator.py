from functools import wraps

def my_deco(func):

    @wraps(func)
    def Wraper():
        print("this is first deco")
        func()
        print("this is first deco")
    return Wraper


@my_deco
def deco():
    print("this is going to be in the middle ")

deco()

    