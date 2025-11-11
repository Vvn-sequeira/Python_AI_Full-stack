
names = ["viivan" , "marcel" , "sequeira" , "rokey"]
bill = [100 , 200 , 300 , 23 ]

for i, j in zip(bill,names):
     print(f"{j} PAID: {i}")

for i in zip(bill,names):
     print(i)