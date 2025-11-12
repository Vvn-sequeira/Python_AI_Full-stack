
Global_var = "Global"


def Global():

    def Local_fun():
       global Global_var  # we are targeting to the global variable " Global_var "
       Global_var = "Local"
    Local_fun()
    print(f"After updating Name : {Global_var}")

Global()


