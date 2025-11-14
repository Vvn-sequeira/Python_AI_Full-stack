
chai_price_in_inr = {
     "masala" : 12,
     "normal" : 10 ,
     "ice coffee" : 50 
}

chai_price_in_usd = {tea:price / 85 for tea , price in chai_price_in_inr.items() }

print(chai_price_in_inr)
print(chai_price_in_usd)