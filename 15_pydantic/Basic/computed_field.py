from pydantic import BaseModel , computed_field , Field

class Booking(BaseModel):

    Cust_id :int 
    room_id : int 
    nights : int = Field(... , ge=1)
    rate_per_night : float

    @computed_field
    @property
    def Total_amount(self) -> float : 
        return self.nights * self.rate_per_night


Total_amt = Booking(Cust_id=123452344 , room_id=101 , nights=2 , rate_per_night=1200 )
print(f"Total Amount : {Total_amt.Total_amount}")