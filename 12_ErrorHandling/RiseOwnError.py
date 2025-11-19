
class NOTFOUNDERROR(Exception):
   pass

def Class(name):
    if name not in ["VIVI" , "marcel" , "vvn" ]:
        raise NOTFOUNDERROR("the name you are searching for is not found in this class !!")
    else:
      print(f"hey , we found {name}  in this class....")

Class("vivi")

print("hey we reached here ....")