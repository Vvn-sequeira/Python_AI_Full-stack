
def Calculate_tax(price , tax):
    return ( price * (100 + tax)/100 )


orders = [100,389,493]

for price in orders:
    print(f"the total amount is after the tax : {Calculate_tax(price,10)}")