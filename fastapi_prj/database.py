from pymongo import MongoClient


username = 'svivianmarcel_db_user'
passwrod = 'V1CdBi1OW0Dyritc'
MongoURL = "mongodb+srv://svivianmarcel_db_user:V1CdBi1OW0Dyritc@medid.0b1jzea.mongodb.net/?appName=MEDID"



client = MongoClient(MongoURL)
DB = client['UserLoginInfo']
collection = DB['Users']
print("MongoDB is connected !!")

