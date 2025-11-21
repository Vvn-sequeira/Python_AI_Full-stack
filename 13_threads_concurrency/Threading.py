import threading
import time 

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1,4):
        print(f"brewing the chai for #{i}")
        time.sleep(3)

# Create a Thread 

order_thread = threading.Thread(target=take_orders)
brewing_chai = threading.Thread(target=brew_chai)

order_thread.start()
brewing_chai.start()

# wait for both to finish 
order_thread.join()
brewing_chai.join()


print("Finished!!")