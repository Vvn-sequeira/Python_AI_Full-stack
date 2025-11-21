import threading
import time

def go_car():
    for i in range(5):
        print(f"#{i} Car is crossing")
        time.sleep(2)

def go_truck():
    for i in range(5):
        print(f"#{i} Truck is crossing ")
        time.sleep(3)

Car_thread = threading.Thread(target=go_car)
Truck_thread = threading.Thread(target=go_truck)

Car_thread.start()
Truck_thread.start()

Car_thread.join()
Truck_thread.join()

print(f"Vehical's are cleared !")
