import threading
import time

def countNo():
    print(f"{threading.current_thread().name} started counting ....")
    count = 0
    for i in range(100_000_000):
        count += 1 
    print(f"{threading.current_thread().name} Finished counting ....")


Thread1 = threading.Thread(target=countNo)
Thread2 = threading.Thread(target=countNo)

StartTime = time.time()
Thread1.start()
Thread2.start()

Thread1.join()
Thread2.join()
EndTime = time.time()

print(f"Time Taken : {EndTime-StartTime}")