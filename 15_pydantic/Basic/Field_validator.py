from pydantic import BaseModel , field_validator


class username(BaseModel):
    name: str 

    @field_validator('name')
    def validator(cls , v):
        if len(v) <= 3 : 
            print( f"Please Enter more that 3 char !!") 
            return

        return v 
    

chekNmae = username(name="vv")
print(chekNmae.name)
