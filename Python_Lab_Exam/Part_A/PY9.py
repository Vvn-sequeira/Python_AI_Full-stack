import random 

s1 = set() 
s2 = set() 

count = 0 

for i in range(10):
    r = random.randint(15,45)
    s1.add(r)

for rn in s1: 
    if rn < 35:
        s2.add(rn)
    if rn < 30: 
        count += 1 
print(f"10 Random Numbeer generated :> {s1}")
print(f"Random Number greater than 35 :> {s2}")
print(f"count of Random Number lesser than 30 :> {count}")
        