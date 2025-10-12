
# u r building a ticket info system for a railway app . based on seat type , show it's features .


Seat_type = input("choose your Seat Type : (Sleeper/AC/general/luxary)").lower()

match Seat_type:
    case "sleeper":
        print(f"No Ac | NO Food | Sleeper Seat | No washroom ")
    case "ac" : 
        print(f"Ac | Sleeper | flexible Seats | WashRoom is available ")
    case "general" :
        print(f"No Seats | Stand and travel ")
    case "luxary":
        print(f"AC | washroom | shower | Sleeping Bed | Private Room | TV | Food | welcome Drinks ")
    case _:
        print(f"Invalid Seat Type  ")
        