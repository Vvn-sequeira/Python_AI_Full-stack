
device_status = input("Status of device ? ")

if device_status == "active" :
    if int(input("what's the temperature ? ")) > 35 : 
        print(f"Hig temperature")
    else :
        print(f"Temperature Normal")
else :
    print(f"Device is offline")
