
import threading
import time 

lock = threading.Lock()

count =0 

def counter():
    global count
    for _ in range(100000):
       with lock:
           count += 1

threads = [threading.Thread(target=counter) for _ in range(10)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f"done counter {count}")