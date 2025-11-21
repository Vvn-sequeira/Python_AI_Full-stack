
from multiprocessing import Process
import time 


def brewing_chai(i):
    print(f"chai brewing started for order no : {i}")
    time.sleep(2)
    print(f"Serving chai for order no : {i}")


if __name__ == "__main__":
   chai_process = [
    Process(target=brewing_chai , args={i+1})
    for i in range(4) 
]

# Start process
   for i in chai_process:
    i.start()

# Wait to complete 
   for p in chai_process:
    p.join()

   print("done!!")