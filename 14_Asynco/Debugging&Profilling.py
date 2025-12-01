
import threading
import time 

#Racd Condition 

stock = 0 

def addStock():
    global stock
    for _ in range(1000000):
        stock += 1 

threads = [threading.Thread(target=addStock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print(f"the available stock is : {stock}")
