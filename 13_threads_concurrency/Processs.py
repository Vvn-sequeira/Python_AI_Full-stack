from MultiProcessing import Process
import time 


def counting():
    print("stated counting >>>>>")
    total = 0 
    for _ in range(10**8):
        total += 1 

    print(f"Done processsing!! ")

if __name__ == "__main__":
   processs = [Process(target=counting) for _ in range(2)]

   start = time.time()
   [p.start() for p in processs]
   [p.join() for p in processs]
   print(f"done ..... time taken is : {time.time() - start:.2f} sec...")
