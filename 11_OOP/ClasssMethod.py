
class Football:

    def __init__(self , pos , no , name):
        self.Position = pos 
        self.JNo = no 
        self.Name = name 

    @classmethod
    def Info(cls, info):
        return cls(info["pos"] , info["no"] , info["name"])
    
info = {
    "pos" : "Back",
    "no" : 90,
    "name" : "vivi" 
}

player_one = Football.Info(info)
print(player_one.__dict__)
        
    
        