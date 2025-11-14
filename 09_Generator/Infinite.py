
def infinite():
    count = 1 
    
    while True:
        yield f"Refile count #{count}"
        count += 1


Coco_cola_user1 = infinite()

for i in range(5):
    print(next(Coco_cola_user1))



