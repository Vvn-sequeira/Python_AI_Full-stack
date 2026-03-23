
class Skywasy: 
    
    fare = int(input("Enter the Fare: "))
    flight_NO = input("Enter the Flight No. : ")
    ticket = int(input("Enter the Ticket : "))
    origin = input("Enter the Origin : ")
    Destiny = input("Enter the Destiny : ")
    iterny = input("Enter the Iterny : ")
    meal = input("Enter the meal options : ")
    
    
    def Display(cls):
        print("Flight Details: ")
        print(f"FLight NO: {getattr(cls,"flight_NO")}")
        print(f"Flight Ticket Price: {getattr(cls,"fare")}")
        print(f"Number of Tickets availabe : {getattr(cls,"ticket")}")
        print(f"FLight Take off from: {getattr(cls,"origin")}")
        print(f"FLight Destiny: {getattr(cls,"Destiny")}")
        print(f"Meals Options : {getattr(cls,"meal")}")
        
        
    def baggage(cls):
        c = input("Enter the Check-IN weight : ") + " KG "
        cabin = input("Enter the Cabin weight : ") + " KG "

        setattr(cls,"CheckIN",c)
        setattr(cls,"CabIn",cabin)

        print("Baggage Details")
        print(f"Check-IN weight : {getattr(cls, "CheckIN")}")
        print(f"Check-IN weight : {getattr(cls, "CabIn")}")
        
    def bookings(self, name , tictes):
        self.name = name 
        self.tickets = tictes
        
        if self.tickets < Skywasy.ticket:
            print(f"Name : {self.name}")
            print(f"Number of Tickets : {self.tickets}")
            Skywasy.ticket = Skywasy.ticket - self.tickets
            print(f"Total Price is : {Skywasy.fare * self.tickets}")
            print(f"Number of Tickets available is : {Skywasy.ticket}")
        else: 
            print(f"Sorry the Titckets are Unavailabe : {Skywasy.ticket}")
        
    
    
s = Skywasy() 
s.Display()

while True: 
    print("\n\n 1. Update the Fare \t 2. Update the Baggage \t 3. Update Iterny \t 4. Book Ticet ")

    ch = int(input("Enter the choice "))

    if ch == 1: 
        New_fare = int(input("Enter new Fare price : "))
        setattr(Skywasy,"fare",New_fare)
        print("fare Updated!")

    elif ch == 2: 
        s.baggage() 
        
    elif ch == 3: 
        New_iterny = input("Enter NEw Iterny: ")
        setattr(Skywasy , 'iterny', New_iterny)
        print("successfully Update!")

    elif ch == 4: 
        name = input("enter the Name of the customer")
        ticets = int(input("No of Tickets ?"))
        s.bookings(name , ticets) 
    
    else : 
        break


        
        
