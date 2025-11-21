
from MultiProcessing import Process
import time 

def counting():
    print(f"{Process.name} started counting ")
    count = 0 
    for i in range(100_000_000):
        count += 1

    print(f"{Process.name} finished his Counting ")

if __name__ == "__main__":
  P1 = Process(target=counting , name= "P1")
  P2 = Process(target=counting , name= "P2")

  St = time.time()

  P1.start()
  P2.start()

  P1.join()
  P2.join()

  ET = time.time() 

  print(f"Process took {ET - St:.2f} sec.... ") 